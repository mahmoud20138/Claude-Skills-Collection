# -*- coding: utf-8 -*-
"""
Trading Dashboard Data Bridge
==============================
Connects to MetaTrader 5 via the MetaTrader5 Python package,
fetches live prices + account data + indicators for all 21 instruments,
and writes output to live_data.json every 5 seconds.

Usage:
    python data_bridge.py

Requirements:
    pip install MetaTrader5 numpy

Notes:
    - MT5 must be installed and logged in before running this script
    - All symbols must have the 'm' suffix as used on Exness
    - The script writes live_data.json in the same directory as this script
"""

import sys
import os
import json
import time
import logging
import traceback
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------------

SYMBOLS = [
    # Gold
    "XAUUSDm",
    # Forex
    "EURUSDm",
    "GBPUSDm",
    "USDJPYm",
    "USDCHFm",
    "AUDUSDm",
    "USDCADm",
    "NZDUSDm",
    "EURGBPm",
    # Indices
    "USTECm",
    "US30m",
    "US500m",
    # Crypto
    "BTCUSDm",
    "ETHUSDm",
    # Stocks
    "AAPLm",
    "MSFTm",
    "AMZNm",
    "GOOGLm",
    "TSLAm",
    "NVDAm",
    "METAm",
]

CATEGORY_MAP = {
    "XAUUSDm": "Gold",
    "EURUSDm": "Forex",
    "GBPUSDm": "Forex",
    "USDJPYm": "Forex",
    "USDCHFm": "Forex",
    "AUDUSDm": "Forex",
    "USDCADm": "Forex",
    "NZDUSDm": "Forex",
    "EURGBPm": "Forex",
    "USTECm": "Indices",
    "US30m": "Indices",
    "US500m": "Indices",
    "BTCUSDm": "Crypto",
    "ETHUSDm": "Crypto",
    "AAPLm": "Stocks",
    "MSFTm": "Stocks",
    "AMZNm": "Stocks",
    "GOOGLm": "Stocks",
    "TSLAm": "Stocks",
    "NVDAm": "Stocks",
    "METAm": "Stocks",
}

UPDATE_INTERVAL_SECONDS = 5
OUTPUT_FILE = Path(__file__).parent / "live_data.json"

# Indicator parameters
RSI_PERIOD = 14
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL_P = 9
EMA_SHORT = 20
EMA_LONG = 50
EMA_HTF = 200
BARS_NEEDED = max(MACD_SLOW + MACD_SIGNAL_P + 5, EMA_HTF + 5, 220)

# ---------------------------------------------------------------------------
# LOGGING
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(Path(__file__).parent / "bridge.log", encoding="utf-8"),
    ],
)
log = logging.getLogger("data_bridge")

# ---------------------------------------------------------------------------
# INDICATOR CALCULATIONS (pure numpy, no TA-Lib required)
# ---------------------------------------------------------------------------


def _ema(prices: list, period: int) -> list:
    """Exponential Moving Average."""
    if len(prices) < period:
        return [None] * len(prices)
    k = 2.0 / (period + 1)
    result = [None] * (period - 1)
    sma = sum(prices[:period]) / period
    result.append(sma)
    for i in range(period, len(prices)):
        result.append(prices[i] * k + result[-1] * (1 - k))
    return result


def calc_rsi(closes: list, period: int = RSI_PERIOD) -> float | None:
    """Returns the most recent RSI value (0-100)."""
    if len(closes) < period + 1:
        return None
    gains, losses = [], []
    for i in range(1, len(closes)):
        d = closes[i] - closes[i - 1]
        gains.append(max(d, 0.0))
        losses.append(max(-d, 0.0))
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return round(100 - 100 / (1 + rs), 2)


def calc_macd(closes: list) -> dict:
    """Returns MACD line, signal line, histogram, and textual signal."""
    if len(closes) < MACD_SLOW + MACD_SIGNAL_P + 2:
        return {"macd": None, "signal": None, "hist": None, "label": "neutral"}

    ema_fast = _ema(closes, MACD_FAST)
    ema_slow = _ema(closes, MACD_SLOW)

    macd_line = []
    for f, s in zip(ema_fast, ema_slow):
        if f is not None and s is not None:
            macd_line.append(f - s)

    if len(macd_line) < MACD_SIGNAL_P + 2:
        return {"macd": None, "signal": None, "hist": None, "label": "neutral"}

    sig_line = _ema(macd_line, MACD_SIGNAL_P)
    macd_now = macd_line[-1]
    sig_now = sig_line[-1]
    macd_prev = macd_line[-2]
    sig_prev = sig_line[-2] if len(sig_line) >= 2 else sig_now

    hist = macd_now - sig_now if (macd_now and sig_now) else None

    # Determine signal label
    if macd_prev is not None and sig_prev is not None:
        if macd_prev < sig_prev and macd_now > sig_now:
            label = "bullish_cross"
        elif macd_prev > sig_prev and macd_now < sig_now:
            label = "bearish_cross"
        elif macd_now > sig_now:
            label = "bullish"
        elif macd_now < sig_now:
            label = "bearish"
        else:
            label = "neutral"
    else:
        label = "neutral"

    return {
        "macd": round(macd_now, 6) if macd_now else None,
        "signal": round(sig_now, 6) if sig_now else None,
        "hist": round(hist, 6) if hist else None,
        "label": label,
    }


def calc_ema_alignment(closes: list) -> str:
    """Returns 'bullish', 'bearish', or 'neutral' based on EMA stack."""
    if len(closes) < EMA_HTF + 2:
        return "neutral"
    e_short = _ema(closes, EMA_SHORT)[-1]
    e_long = _ema(closes, EMA_LONG)[-1]
    e_htf = _ema(closes, EMA_HTF)[-1]
    if None in (e_short, e_long, e_htf):
        return "neutral"
    price = closes[-1]
    if price > e_short > e_long > e_htf:
        return "bullish"
    if price < e_short < e_long < e_htf:
        return "bearish"
    return "neutral"


def calc_atr(highs: list, lows: list, closes: list, period: int = 14) -> float | None:
    """Average True Range."""
    if len(closes) < period + 1:
        return None
    trs = []
    for i in range(1, len(closes)):
        tr = max(
            highs[i] - lows[i],
            abs(highs[i] - closes[i - 1]),
            abs(lows[i] - closes[i - 1]),
        )
        trs.append(tr)
    if len(trs) < period:
        return None
    atr = sum(trs[-period:]) / period
    return round(atr, 6)


def calc_confluence_score(
    rsi: float, macd_label: str, ema_align: str, trend: str, change_pct: float
) -> int:
    """
    Simple confluence scoring system (0-10).
    Mimics the ICT multi-factor scoring used in the MQL5 indicator.
    """
    score = 0

    # HTF trend alignment
    if ema_align in ("bullish", "bearish"):
        score += 2

    # EMA + trend match
    if ema_align == "bullish" and trend == "bullish":
        score += 1
    elif ema_align == "bearish" and trend == "bearish":
        score += 1

    # RSI zone
    if rsi is not None:
        if 40 <= rsi <= 60:
            pass  # neutral zone = no extra score
        elif 60 < rsi < 70:
            score += 1  # bullish momentum
        elif 30 < rsi < 40:
            score += 1  # bearish momentum
        elif rsi >= 70:
            pass  # overbought
        elif rsi <= 30:
            pass  # oversold

    # MACD cross = strong signal
    if macd_label in ("bullish_cross", "bearish_cross"):
        score += 2
    elif macd_label in ("bullish", "bearish"):
        score += 1

    # Price momentum
    if abs(change_pct) > 0.5:
        score += 1
    if abs(change_pct) > 1.5:
        score += 1

    return min(score, 10)


def determine_trend(ema_align: str, macd_label: str, rsi: float) -> str:
    """Derive overall trend from indicator combination."""
    bull_count = sum(
        [
            ema_align == "bullish",
            "bullish" in macd_label,
            rsi is not None and rsi > 55,
        ]
    )
    bear_count = sum(
        [
            ema_align == "bearish",
            "bearish" in macd_label,
            rsi is not None and rsi < 45,
        ]
    )
    if bull_count >= 2:
        return "bullish"
    if bear_count >= 2:
        return "bearish"
    return "neutral"


# ---------------------------------------------------------------------------
# MT5 CONNECTION
# ---------------------------------------------------------------------------


def connect_mt5() -> bool:
    """Initialize MT5 connection. Returns True on success."""
    try:
        import MetaTrader5 as mt5  # type: ignore

        if not mt5.initialize():
            log.error(f"MT5 initialize() failed — error: {mt5.last_error()}")
            return False
        info = mt5.account_info()
        if info is None:
            log.error("Could not retrieve account info. Is MT5 logged in?")
            return False
        log.info(
            f"MT5 connected — Account #{info.login} | Balance: {info.balance:.2f} {info.currency}"
        )
        return True
    except ImportError:
        log.error("MetaTrader5 package not installed. Run: pip install MetaTrader5")
        return False


def get_account_info() -> dict:
    """Fetch live account data from MT5."""
    import MetaTrader5 as mt5  # type: ignore

    info = mt5.account_info()
    if info is None:
        return {}
    balance = info.balance
    equity = info.equity
    margin = info.margin
    free_m = info.margin_free
    m_level = (
        info.margin_level
        if info.margin_level
        else (equity / margin * 100 if margin > 0 else 0)
    )
    profit = equity - balance
    return {
        "balance": round(balance, 2),
        "equity": round(equity, 2),
        "margin": round(margin, 2),
        "free_margin": round(free_m, 2),
        "margin_level": round(m_level, 2),
        "profit": round(profit, 2),
        "daily_pnl": round(
            profit, 2
        ),  # Approximate: full daily PnL needs trade history
        "daily_pnl_pct": round(profit / balance, 6) if balance else 0.0,
    }


def get_symbol_data(symbol: str) -> dict | None:
    """Fetch tick + OHLCV data and compute indicators for a single symbol."""
    import MetaTrader5 as mt5  # type: ignore

    # Enable symbol in Market Watch if needed
    if not mt5.symbol_select(symbol, True):
        log.warning(f"Could not select symbol: {symbol}")
        return None

    # Current tick
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        log.warning(f"No tick data for {symbol}")
        return None

    # Symbol info for digits / spread
    sym_info = mt5.symbol_info(symbol)
    if sym_info is None:
        return None

    bid = tick.bid
    ask = tick.ask
    spread_raw = ask - bid
    digits = sym_info.digits
    point = sym_info.point
    spread_pts = round(spread_raw / point) if point > 0 else 0

    # Historical bars for indicators (H1 timeframe)
    bars = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_H1, 0, BARS_NEEDED)
    if bars is None or len(bars) < 50:
        log.warning(f"Not enough bars for {symbol} ({len(bars) if bars else 0} bars)")
        return {
            "symbol": symbol,
            "category": CATEGORY_MAP.get(symbol, "Unknown"),
            "bid": round(bid, digits),
            "ask": round(ask, digits),
            "spread": round(spread_raw, digits),
            "change_pct": 0.0,
            "trend": "neutral",
            "rsi": 50.0,
            "macd_signal": "neutral",
            "ema_alignment": "neutral",
            "confluence_score": 0,
            "atr": None,
        }

    closes = [float(b["close"]) for b in bars]
    highs = [float(b["high"]) for b in bars]
    lows = [float(b["low"]) for b in bars]

    # Change % vs 24h ago (approx 24 bars back on H1)
    lookback = min(24, len(closes) - 1)
    prev_price = closes[-(lookback + 1)]
    change_pct = (
        ((closes[-1] - prev_price) / prev_price * 100) if prev_price != 0 else 0.0
    )

    rsi = calc_rsi(closes)
    macd_d = calc_macd(closes)
    ema_align = calc_ema_alignment(closes)
    atr = calc_atr(highs, lows, closes)
    trend = determine_trend(ema_align, macd_d["label"], rsi or 50.0)
    score = calc_confluence_score(
        rsi or 50.0, macd_d["label"], ema_align, trend, change_pct
    )

    return {
        "symbol": symbol,
        "category": CATEGORY_MAP.get(symbol, "Unknown"),
        "bid": round(bid, digits),
        "ask": round(ask, digits),
        "spread": round(spread_raw, digits + 1),
        "change_pct": round(change_pct, 3),
        "trend": trend,
        "rsi": rsi,
        "macd_signal": macd_d["label"],
        "ema_alignment": ema_align,
        "confluence_score": score,
        "atr": round(atr, digits + 1) if atr else None,
    }


def get_open_positions() -> list:
    """Fetch all open MT5 positions with calculated metrics."""
    import MetaTrader5 as mt5  # type: ignore

    positions = mt5.positions_get()
    if positions is None:
        return []

    result = []
    for p in positions:
        # Point value for pips
        sym_info = mt5.symbol_info(p.symbol)
        if sym_info is None:
            continue
        point = sym_info.point
        digits = sym_info.digits

        # Pips
        raw_diff = (
            p.price_current - p.price_open
            if p.type == mt5.ORDER_TYPE_BUY
            else p.price_open - p.price_current
        )
        pips = round(raw_diff / point) if point else 0

        # R-multiple
        sl_dist = abs(p.price_open - p.sl) if p.sl else None
        tp_dist = abs(p.tp - p.price_open) if p.tp else None
        if sl_dist and sl_dist > 0:
            r_multiple = raw_diff / sl_dist
        else:
            r_multiple = 0.0

        result.append(
            {
                "ticket": p.ticket,
                "symbol": p.symbol,
                "type": "BUY" if p.type == mt5.ORDER_TYPE_BUY else "SELL",
                "volume": round(p.volume, 2),
                "price_open": round(p.price_open, digits),
                "price_current": round(p.price_current, digits),
                "sl": round(p.sl, digits) if p.sl else None,
                "tp": round(p.tp, digits) if p.tp else None,
                "profit": round(p.profit, 2),
                "pips": pips,
                "r_multiple": round(r_multiple, 2),
                "time_open": datetime.fromtimestamp(p.time, tz=timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "comment": p.comment,
                "magic": p.magic,
            }
        )

    return result


def get_session_info() -> dict:
    """Determine current trading session based on UTC time."""
    h = datetime.now(tz=timezone.utc).hour
    m = datetime.now(tz=timezone.utc).minute

    if 8 <= h < 12 or (h == 12 and m == 0):
        session = "London"
        kz = 8 <= h < 11
    elif h == 12 or (12 < h < 13):
        session = "London/New York Overlap"
        kz = True
    elif 13 <= h < 22:
        session = "New York"
        kz = 13 <= h < 17
    else:
        session = "Asian"
        kz = h >= 23 or h < 3

    return {
        "current": session,
        "killzone_active": kz,
        "next_event": "None",
        "server_time": datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
    }


def generate_signals_from_instruments(instruments: list) -> list:
    """
    Generate simple rule-based signals from scanned instrument data.
    Only produces signals for instruments with score >= 6.
    """
    signals = []
    now_iso = datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")

    for inst in sorted(
        instruments, key=lambda x: x.get("confluence_score", 0), reverse=True
    ):
        score = inst.get("confluence_score", 0)
        if score < 6:
            continue

        trend = inst.get("trend", "neutral")
        if trend == "neutral":
            continue

        direction = "BUY" if trend == "bullish" else "SELL"
        bid = inst.get("bid", 0)
        atr = inst.get("atr") or (bid * 0.001)  # fallback: 0.1% ATR

        entry = bid
        if direction == "BUY":
            sl = round(entry - 1.5 * atr, 5)
            tp = round(entry + 3.0 * atr, 5)
        else:
            sl = round(entry + 1.5 * atr, 5)
            tp = round(entry - 3.0 * atr, 5)

        factors = []
        if inst.get("ema_alignment") in ("bullish", "bearish"):
            factors.append("EMA_Align")
        if inst.get("macd_signal") in ("bullish_cross", "bearish_cross"):
            factors.append("MACD_Cross")
        elif inst.get("macd_signal") in ("bullish", "bearish"):
            factors.append("MACD_Dir")
        rsi = inst.get("rsi", 50)
        if rsi is not None:
            if direction == "BUY" and 50 < rsi < 70:
                factors.append("RSI_Bull")
            elif direction == "SELL" and 30 < rsi < 50:
                factors.append("RSI_Bear")
        if score >= 8:
            factors.extend(["HTF_Bias", "Killzone"])
        if score >= 7:
            factors.append("Momentum")

        strategy_parts = []
        if "MACD_Cross" in factors:
            strategy_parts.append("MACD_X")
        if "EMA_Align" in factors:
            strategy_parts.append("EMA")
        strategy_parts.append(f"Score{score}")

        signals.append(
            {
                "timestamp": now_iso,
                "type": "SIGNAL",
                "symbol": inst["symbol"],
                "direction": direction,
                "score": score,
                "strategy": "+".join(strategy_parts)
                if strategy_parts
                else "Multi-Factor",
                "entry": entry,
                "sl": sl,
                "tp": tp,
                "factors": factors[:8],
            }
        )

    return signals[:15]  # cap at 15 signals


# ---------------------------------------------------------------------------
# MAIN LOOP
# ---------------------------------------------------------------------------


def build_payload(
    account: dict, instruments: list, positions: list, session: dict
) -> dict:
    signals = generate_signals_from_instruments(instruments)

    # Basic stats from positions
    closed_today = []  # Would need trade history for real stats
    win_rate = 68.5  # Placeholder — needs trade history from MT5
    avg_rr = 2.15  # Placeholder

    return {
        "timestamp": datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z"),
        "account": account,
        "instruments": instruments,
        "positions": positions,
        "signals": signals,
        "session": session,
        "stats": {
            "win_rate": win_rate,
            "avg_rr": avg_rr,
            "today_trades": len(positions),
            "total_signals_today": len(signals),
        },
    }


def write_json(data: dict) -> None:
    tmp_path = OUTPUT_FILE.with_suffix(".tmp")
    try:
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        tmp_path.replace(OUTPUT_FILE)
        log.info(
            f"live_data.json updated — {len(data['instruments'])} symbols, "
            f"{len(data['positions'])} positions, {len(data['signals'])} signals"
        )
    except Exception as e:
        log.error(f"Failed to write JSON: {e}")
        if tmp_path.exists():
            tmp_path.unlink(missing_ok=True)


# ---------------------------------------------------------------------------
# BUILT-IN HTTP SERVER (serves dashboard + live_data.json)
# ---------------------------------------------------------------------------

import threading
import http.server
import webbrowser
import functools

HTTP_PORT = 8888
DASHBOARD_DIR = Path(__file__).parent


class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    """Serves files from the dashboard directory with proper CORS and caching headers."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DASHBOARD_DIR), **kwargs)

    def end_headers(self):
        # Allow all origins (local use only)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        # Prevent caching of live_data.json
        if "live_data" in self.path:
            self.send_header(
                "Cache-Control", "no-store, no-cache, must-revalidate, max-age=0"
            )
            self.send_header("Pragma", "no-cache")
            self.send_header("Expires", "0")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        # Silence HTTP request logs (too noisy with 5s refresh)
        pass


def start_http_server():
    """Start the HTTP server on a background thread."""
    handler = DashboardHandler
    try:
        server = http.server.HTTPServer(("0.0.0.0", HTTP_PORT), handler)
        log.info(f"HTTP server started at http://localhost:{HTTP_PORT}")
        server.serve_forever()
    except OSError as e:
        if "Address already in use" in str(e) or "10048" in str(e):
            log.warning(f"Port {HTTP_PORT} already in use -- trying {HTTP_PORT + 1}")
            try:
                server = http.server.HTTPServer(("0.0.0.0", HTTP_PORT + 1), handler)
                log.info(f"HTTP server started at http://localhost:{HTTP_PORT + 1}")
                server.serve_forever()
            except Exception as e2:
                log.error(f"Could not start HTTP server: {e2}")
        else:
            log.error(f"HTTP server error: {e}")


# ---------------------------------------------------------------------------
# MAIN LOOP
# ---------------------------------------------------------------------------


def run_loop() -> None:
    log.info("")
    log.info("=" * 64)
    log.info("  TRADING COMMAND CENTER - Data Bridge + HTTP Server")
    log.info("=" * 64)
    log.info(f"  Dashboard URL : http://localhost:{HTTP_PORT}")
    log.info(f"  Data output   : {OUTPUT_FILE}")
    log.info(f"  Symbols       : {len(SYMBOLS)}")
    log.info(f"  Refresh       : every {UPDATE_INTERVAL_SECONDS}s")
    log.info("=" * 64)
    log.info("")

    # 1. Start HTTP server on background thread
    http_thread = threading.Thread(target=start_http_server, daemon=True)
    http_thread.start()
    time.sleep(0.5)  # Let server bind

    # 2. Open browser automatically
    dashboard_url = f"http://localhost:{HTTP_PORT}/index.html"
    log.info(f"Opening dashboard in browser: {dashboard_url}")
    try:
        webbrowser.open(dashboard_url)
    except Exception:
        log.warning("Could not auto-open browser. Open manually:")
        log.warning(f"  --> {dashboard_url}")

    # 3. Connect to MT5
    connected = connect_mt5()
    if not connected:
        log.warning("")
        log.warning("MT5 not available -- serving static sample data.")
        log.warning("Dashboard is still accessible at:")
        log.warning(f"  --> {dashboard_url}")
        log.warning("")
        log.warning("Press Ctrl+C to stop.")
        # Keep server running even without MT5
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            return
        return

    import MetaTrader5 as mt5  # type: ignore

    log.info("")
    log.info("LIVE MODE ACTIVE -- MT5 data streaming to dashboard")
    log.info("Press Ctrl+C to stop.")
    log.info("")

    iteration = 0
    while True:
        iteration += 1
        start_time = time.monotonic()

        try:
            # 1. Account info
            account = get_account_info()

            # 2. Instrument data + indicators
            instruments = []
            for sym in SYMBOLS:
                data = get_symbol_data(sym)
                if data:
                    instruments.append(data)

            # 3. Open positions
            positions = get_open_positions()

            # 4. Session
            session = get_session_info()

            # 5. Assemble & write
            payload = build_payload(account, instruments, positions, session)
            write_json(payload)

        except Exception as exc:
            log.error(f"Iteration {iteration} error: {exc}")
            log.debug(traceback.format_exc())

        # Sleep for remainder of interval
        elapsed = time.monotonic() - start_time
        sleep_for = max(0.1, UPDATE_INTERVAL_SECONDS - elapsed)
        log.debug(
            f"Iteration {iteration} took {elapsed:.2f}s -- sleeping {sleep_for:.2f}s"
        )
        time.sleep(sleep_for)


# ---------------------------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        run_loop()
    except KeyboardInterrupt:
        log.info("")
        log.info("Data bridge stopped by user (Ctrl+C).")
    except Exception as e:
        log.critical(f"Fatal error: {e}")
        log.critical(traceback.format_exc())
        sys.exit(1)

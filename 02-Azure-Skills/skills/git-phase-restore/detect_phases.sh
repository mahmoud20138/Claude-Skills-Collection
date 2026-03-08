#!/usr/bin/env bash
# detect_phases.sh — Analyze Git history and output structured phase information
# Usage: bash detect_phases.sh [repo-path]
# If no path given, uses current directory.

set -euo pipefail

REPO="${1:-.}"
cd "$REPO"

# Verify git repo
if ! git rev-parse --is-inside-work-tree &>/dev/null; then
    echo "ERROR: Not a Git repository: $REPO"
    exit 1
fi

DIVIDER="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

echo ""
echo "PROJECT PHASE ANALYSIS"
echo "$DIVIDER"
echo "Repository: $(basename "$(git rev-parse --show-toplevel)")"
echo "Current branch: $(git branch --show-current 2>/dev/null || echo 'detached HEAD')"
echo "Total commits: $(git rev-list --count HEAD 2>/dev/null || echo '0')"
echo "Analyzed on: $(date '+%Y-%m-%d %H:%M:%S')"
echo "$DIVIDER"
echo ""

# ── Section 1: Tags (explicit milestones) ────────────────────────────────
echo "TAGS (Explicit Milestones)"
echo "──────────────────────────"
TAG_COUNT=$(git tag -l | wc -l | tr -d ' ')
if [ "$TAG_COUNT" -gt 0 ]; then
    git tag -l --sort=creatordate --format='  %(creatordate:short)  %(refname:short)  %(subject)' | while read -r line; do
        echo "$line"
    done
else
    echo "  (no tags found)"
fi
echo ""

# ── Section 2: Branches (development tracks) ─────────────────────────────
echo "BRANCHES (Development Tracks)"
echo "─────────────────────────────"
echo "  Active:"
git branch --sort=-committerdate --format='    %(committerdate:short)  %(refname:short)' | head -20
MERGED=$(git branch --merged main 2>/dev/null || git branch --merged master 2>/dev/null || echo "")
if [ -n "$MERGED" ]; then
    echo ""
    echo "  Merged (completed phases):"
    echo "$MERGED" | while read -r branch; do
        branch=$(echo "$branch" | tr -d ' *')
        [ -z "$branch" ] && continue
        [ "$branch" = "main" ] || [ "$branch" = "master" ] && continue
        last_date=$(git log -1 --format='%ad' --date=short "$branch" 2>/dev/null || echo "unknown")
        echo "    $last_date  $branch"
    done
fi
echo ""

# ── Section 3: Semantic commit phases ─────────────────────────────────────
echo "COMMIT PHASES (Semantic Analysis)"
echo "──────────────────────────────────"

# Group commits by conventional commit type and time proximity
prev_type=""
prev_date=""
phase_num=0
phase_start=""
phase_commits=0
phase_label=""

print_phase() {
    if [ "$phase_num" -gt 0 ] && [ -n "$phase_label" ]; then
        echo "  Phase $phase_num: $phase_label"
        echo "    Range: $phase_start → $prev_date ($phase_commits commits)"
    fi
}

git log --reverse --format='%h %ad %s' --date=short | while IFS= read -r line; do
    hash=$(echo "$line" | awk '{print $1}')
    date=$(echo "$line" | awk '{print $2}')
    msg=$(echo "$line" | cut -d' ' -f3-)

    # Detect commit type
    type="other"
    case "$msg" in
        feat:*|feat\(*) type="feat" ;;
        fix:*|fix\(*)   type="fix" ;;
        refactor:*|refactor\(*) type="refactor" ;;
        chore:*|chore\(*) type="chore" ;;
        docs:*|docs\(*)  type="docs" ;;
        test:*|test\(*)  type="test" ;;
        perf:*|perf\(*)  type="perf" ;;
        style:*|style\(*) type="style" ;;
        ci:*|ci\(*)      type="ci" ;;
        Merge*|merge*)   type="merge" ;;
        Initial*|initial*|init*) type="init" ;;
    esac

    # Detect phase boundary: type changes, or >3 day gap, or merge commit
    is_boundary=false
    if [ -z "$prev_type" ]; then
        is_boundary=true
    elif [ "$type" = "merge" ]; then
        is_boundary=true
    elif [ "$type" != "$prev_type" ] && [ "$type" != "other" ] && [ "$prev_type" != "other" ]; then
        is_boundary=true
    elif [ -n "$prev_date" ] && [ "$date" != "$prev_date" ]; then
        # Check if dates are more than 3 days apart
        if command -v python3 &>/dev/null; then
            gap=$(python3 -c "
from datetime import datetime
d1 = datetime.strptime('$prev_date', '%Y-%m-%d')
d2 = datetime.strptime('$date', '%Y-%m-%d')
print((d2-d1).days)
" 2>/dev/null || echo "0")
            [ "$gap" -gt 3 ] && is_boundary=true
        fi
    fi

    if [ "$is_boundary" = true ]; then
        print_phase
        phase_num=$((phase_num + 1))
        phase_start="$date"
        phase_commits=0

        # Generate phase label from commit message
        case "$type" in
            init)     phase_label="Project Init" ;;
            feat)     phase_label=$(echo "$msg" | sed 's/^feat[:(][^)]*[)]\?:\? *//' | head -c 40) ;;
            fix)      phase_label="Bug Fixes" ;;
            refactor) phase_label=$(echo "$msg" | sed 's/^refactor[:(][^)]*[)]\?:\? *//' | head -c 40) ;;
            merge)    phase_label=$(echo "$msg" | sed 's/^Merge.*branch .//;s/.//' | head -c 40) ;;
            chore)    phase_label="Maintenance" ;;
            *)        phase_label=$(echo "$msg" | head -c 40) ;;
        esac
    fi

    phase_commits=$((phase_commits + 1))
    prev_type="$type"
    prev_date="$date"
done

# Print last phase
# (handled by subshell — we re-print summary below)

echo ""

# ── Section 4: Full timeline (compact) ────────────────────────────────────
echo "FULL TIMELINE (last 30 commits)"
echo "────────────────────────────────"
git log --oneline --graph --decorate -30
echo ""

# ── Section 5: Working tree status ────────────────────────────────────────
echo "CURRENT STATUS"
echo "──────────────"
DIRTY=$(git status --porcelain | wc -l | tr -d ' ')
if [ "$DIRTY" -gt 0 ]; then
    echo "  ⚠  Working tree has $DIRTY uncommitted change(s)"
    git status --short | head -10 | sed 's/^/  /'
    [ "$DIRTY" -gt 10 ] && echo "  ... and $((DIRTY - 10)) more"
else
    echo "  ✓  Working tree is clean"
fi

STASH_COUNT=$(git stash list | wc -l | tr -d ' ')
if [ "$STASH_COUNT" -gt 0 ]; then
    echo "  📦 $STASH_COUNT stash(es) found:"
    git stash list | head -5 | sed 's/^/  /'
fi
echo ""

echo "$DIVIDER"
echo "Run 'git reflog' to see full navigation history (safety net)"
echo "$DIVIDER"

#!/usr/bin/env bash
# safe_restore.sh — Safely restore a Git project to a target commit
# Usage: bash safe_restore.sh <target> [strategy]
#   target:   commit hash, tag, branch, or date (YYYY-MM-DD)
#   strategy: inspect | branch | reset | revert (default: branch)

set -euo pipefail

TARGET="${1:?Usage: safe_restore.sh <target> [strategy]}"
STRATEGY="${2:-branch}"

# Verify git repo
if ! git rev-parse --is-inside-work-tree &>/dev/null; then
    echo "ERROR: Not inside a Git repository"
    exit 1
fi

DIVIDER="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# ── Resolve target to a commit hash ──────────────────────────────────────

resolve_target() {
    local input="$1"

    # Try as-is (hash, tag, branch)
    if git rev-parse --verify "$input^{commit}" &>/dev/null; then
        git rev-parse --verify "$input^{commit}"
        return 0
    fi

    # Try as a date
    if [[ "$input" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2} ]]; then
        local found
        found=$(git rev-list -1 --before="$input" HEAD 2>/dev/null || true)
        if [ -n "$found" ]; then
            echo "$found"
            return 0
        fi
    fi

    # Try as a grep on commit messages
    local found
    found=$(git log --all --grep="$input" --format='%H' -1 2>/dev/null || true)
    if [ -n "$found" ]; then
        echo "$found"
        return 0
    fi

    echo ""
    return 1
}

COMMIT=$(resolve_target "$TARGET")
if [ -z "$COMMIT" ]; then
    echo "ERROR: Could not resolve target '$TARGET' to a commit"
    echo ""
    echo "Try one of:"
    echo "  - A commit hash:  abc1234"
    echo "  - A tag:          v1.0.0"
    echo "  - A branch:       feature/auth"
    echo "  - A date:         2025-01-15"
    echo "  - A keyword:      authentication"
    exit 1
fi

SHORT=$(git rev-parse --short "$COMMIT")
ORIGINAL_HEAD=$(git rev-parse HEAD)
ORIGINAL_SHORT=$(git rev-parse --short HEAD)
ORIGINAL_BRANCH=$(git branch --show-current 2>/dev/null || echo "detached")
COMMIT_MSG=$(git log -1 --format='%s' "$COMMIT")
COMMIT_DATE=$(git log -1 --format='%ad' --date=short "$COMMIT")

echo ""
echo "GIT PHASE RESTORE"
echo "$DIVIDER"
echo "Target:   $SHORT ($COMMIT_DATE) $COMMIT_MSG"
echo "Current:  $ORIGINAL_SHORT on '$ORIGINAL_BRANCH'"
echo "Strategy: $STRATEGY"
echo "$DIVIDER"
echo ""

# ── Safety: handle dirty working tree ────────────────────────────────────

DIRTY=$(git status --porcelain | wc -l | tr -d ' ')
if [ "$DIRTY" -gt 0 ]; then
    STASH_MSG="auto-stash before restore to $SHORT ($(date +%Y%m%d_%H%M%S))"
    echo "⚠  Working tree dirty ($DIRTY changes). Auto-stashing..."
    git stash push -m "$STASH_MSG"
    echo "   Stashed as: '$STASH_MSG'"
    echo "   Recover with: git stash pop"
    echo ""
fi

# ── Execute the chosen strategy ──────────────────────────────────────────

case "$STRATEGY" in

    inspect)
        echo "→ Checking out $SHORT in detached HEAD mode (read-only inspection)"
        git checkout "$COMMIT"
        echo ""
        echo "✓ Now viewing commit $SHORT"
        echo "  Return with: git checkout $ORIGINAL_BRANCH"
        echo "  Or:          git checkout -"
        ;;

    branch)
        # Generate a meaningful branch name
        LABEL=$(echo "$COMMIT_MSG" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | head -c 30 | sed 's/-$//')
        BRANCH_NAME="restore/${LABEL}-${SHORT}"

        echo "→ Creating branch '$BRANCH_NAME' from $SHORT"
        git checkout -b "$BRANCH_NAME" "$COMMIT"
        echo ""
        echo "✓ Now on branch '$BRANCH_NAME'"
        echo "  Continue developing from this phase, or merge back when ready."
        echo "  Return with: git checkout $ORIGINAL_BRANCH"
        ;;

    reset)
        echo "⚠  HARD RESET — this moves '$ORIGINAL_BRANCH' to $SHORT"
        echo "   Original HEAD ($ORIGINAL_SHORT) will be in reflog for 90 days"
        echo ""
        git reset --hard "$COMMIT"
        echo ""
        echo "✓ Branch '$ORIGINAL_BRANCH' now points to $SHORT"
        echo "  Undo with: git reset --hard $ORIGINAL_HEAD"
        echo "  Or check:  git reflog"
        ;;

    revert)
        echo "→ Reverting commits from $SHORT to $ORIGINAL_SHORT"
        RANGE="$COMMIT..$ORIGINAL_HEAD"
        RANGE_COUNT=$(git rev-list --count "$RANGE")
        echo "   Reverting $RANGE_COUNT commit(s)..."
        echo ""

        if git revert --no-commit "$RANGE" 2>/dev/null; then
            git commit -m "revert: undo $RANGE_COUNT commits back to $SHORT ($COMMIT_MSG)"
            echo ""
            echo "✓ Reverted $RANGE_COUNT commits. History preserved."
            echo "  Undo with: git revert HEAD"
        else
            echo "⚠  Revert had conflicts. Aborting."
            git revert --abort 2>/dev/null || true
            echo "  Try 'branch' strategy instead: bash safe_restore.sh $TARGET branch"
        fi
        ;;

    *)
        echo "ERROR: Unknown strategy '$STRATEGY'"
        echo "  Valid strategies: inspect, branch, reset, revert"
        exit 1
        ;;
esac

echo ""
echo "$DIVIDER"
echo "POST-RESTORE STATUS"
echo "$DIVIDER"
echo "HEAD: $(git log -1 --oneline)"
echo "Branch: $(git branch --show-current 2>/dev/null || echo 'detached HEAD')"

# Show what changed
DIFF_STAT=$(git diff --stat "$ORIGINAL_HEAD" HEAD 2>/dev/null || echo "(no diff available)")
if [ -n "$DIFF_STAT" ] && [ "$DIFF_STAT" != "(no diff available)" ]; then
    echo ""
    echo "Changes from original state:"
    echo "$DIFF_STAT" | head -15
fi

echo ""
echo "Safety net:"
echo "  git reflog              # full undo history"
echo "  git stash list          # stashed work"
echo "  git checkout -          # go back to previous"
echo "$DIVIDER"

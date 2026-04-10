#!/usr/bin/env bash
set -e

PLUGIN_DIR="$(cd "$(dirname "$0")" && pwd)"
MARKETPLACE_NAME="content-analysis-plugin"
PLUGIN_NAME="content-analysis"

echo "Adding local marketplace from: $PLUGIN_DIR"
claude plugin marketplace add "$PLUGIN_DIR" --name "$MARKETPLACE_NAME"

echo "Installing $PLUGIN_NAME..."
claude plugin install "$PLUGIN_NAME@$MARKETPLACE_NAME"

echo "Done. Restart Claude Code, then use /content-analysis in any project."

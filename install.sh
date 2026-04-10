#!/usr/bin/env bash
set -e

PLUGIN_DIR="$(cd "$(dirname "$0")" && pwd)"
MARKETPLACE_DIR="$HOME/.claude/local-plugin-marketplace"
MARKETPLACE_NAME="local-plugins"
PLUGIN_NAME="content-analysis"

# Create marketplace wrapper
mkdir -p "$MARKETPLACE_DIR/.claude-plugin"
mkdir -p "$MARKETPLACE_DIR/plugins"

# Link the plugin into the marketplace
rm -f "$MARKETPLACE_DIR/plugins/$PLUGIN_NAME"
ln -s "$PLUGIN_DIR" "$MARKETPLACE_DIR/plugins/$PLUGIN_NAME"

# Write marketplace.json
cat > "$MARKETPLACE_DIR/.claude-plugin/marketplace.json" << EOF
{
  "\$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "$MARKETPLACE_NAME",
  "description": "Local Claude Code plugins",
  "owner": {
    "name": "local"
  },
  "plugins": [
    {
      "name": "$PLUGIN_NAME",
      "description": "Scientific content analysis for academic research",
      "source": "./plugins/$PLUGIN_NAME",
      "category": "productivity"
    }
  ]
}
EOF

echo "Adding local marketplace from: $PLUGIN_DIR"
claude plugin marketplace add "$MARKETPLACE_DIR" 2>/dev/null || true

echo "Installing $PLUGIN_NAME..."
claude plugin install "$PLUGIN_NAME@$MARKETPLACE_NAME"

echo "Done. Restart Claude Code, then use /content-analysis in any project."

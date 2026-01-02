#!/bin/bash

# Habit Tracker Uninstall Script
# Stops the service and removes the Launch Agent (keeps your data)

PLIST_NAME="com.local.habit-tracker.plist"
PLIST_DEST="$HOME/Library/LaunchAgents/$PLIST_NAME"

echo ""
echo "🌱 Habit Tracker Uninstall"
echo "=========================="
echo ""

if [ -f "$PLIST_DEST" ]; then
    echo "⏹  Stopping service..."
    launchctl unload "$PLIST_DEST" 2>/dev/null || true
    
    echo "🗑  Removing launch agent..."
    rm "$PLIST_DEST"
    
    echo ""
    echo "✅ Service stopped and removed."
    echo ""
    echo "   Your habit data is still saved in habits.json"
    echo "   To reinstall later, run: ./setup.sh"
    echo ""
else
    echo "ℹ️  No launch agent found. Nothing to uninstall."
fi

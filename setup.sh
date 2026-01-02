#!/bin/bash

# Habit Tracker Setup Script
# This script installs the habit tracker as a background service on macOS

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PLIST_NAME="com.local.habit-tracker.plist"
PLIST_SOURCE="$SCRIPT_DIR/$PLIST_NAME"
PLIST_DEST="$HOME/Library/LaunchAgents/$PLIST_NAME"

echo ""
echo "🌱 Habit Tracker Setup"
echo "======================"
echo ""

# Check if plist template exists
if [ ! -f "$PLIST_SOURCE" ]; then
    echo "❌ Error: $PLIST_NAME not found in $SCRIPT_DIR"
    exit 1
fi

# Create LaunchAgents directory if it doesn't exist
mkdir -p "$HOME/Library/LaunchAgents"

# Stop existing service if running
if launchctl list | grep -q "com.local.habit-tracker"; then
    echo "⏹  Stopping existing service..."
    launchctl unload "$PLIST_DEST" 2>/dev/null || true
fi

# Create the plist with the correct path
echo "📝 Creating launch agent..."
sed "s|__HABIT_TRACKER_PATH__|$SCRIPT_DIR|g" "$PLIST_SOURCE" > "$PLIST_DEST"

# Load the service
echo "🚀 Starting service..."
launchctl load "$PLIST_DEST"

# Wait a moment for the server to start
sleep 1

# Check if it's running
if launchctl list | grep -q "com.local.habit-tracker"; then
    echo ""
    echo "✅ Success! Habit Tracker is now running."
    echo ""
    echo "   Open in browser:  http://localhost:8765"
    echo "   Data stored in:   $SCRIPT_DIR/habits.json"
    echo ""
    echo "   The server will start automatically when you log in."
    echo ""
    echo "   To stop the service:    ./uninstall.sh"
    echo "   To view logs:           cat $SCRIPT_DIR/server.log"
    echo ""
else
    echo ""
    echo "❌ Something went wrong. Check the logs:"
    echo "   cat $SCRIPT_DIR/server.log"
    exit 1
fi

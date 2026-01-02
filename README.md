# Habit Tracker

A simple, local habit tracker that saves your data to a JSON file on your computer.

## Quick Start (Auto-Start on Login)

1. Move this folder somewhere permanent (e.g. `~/Apps/habit-tracker`)
2. Open Terminal and navigate to the folder:
   ```bash
   cd ~/Apps/habit-tracker
   ```
3. Run the setup script:
   ```bash
   chmod +x setup.sh uninstall.sh
   ./setup.sh
   ```
4. Open http://localhost:8765 in your browser
5. **Bookmark it!** — Add to your bookmarks bar for one-click access

The server now runs in the background and starts automatically when you log in.

## Easy Browser Access

For quickest access, create a bookmark:
- **URL:** `http://localhost:8765`
- **Name:** Habits (or add an emoji: 🌱 Habits)
- Drag it to your bookmarks bar

You could also set it as your browser homepage or new tab page.

## Manual Start (Alternative)

If you prefer to run it manually:

```bash
cd ~/Apps/habit-tracker
python3 server.py
```

Then open http://localhost:8765

## How It Works

- **Add habits** using the input field at the top
- **Click day buttons** to cycle through: empty → ✓ (completed) → ✗ (missed) → empty
- **Today** is highlighted with an orange ring
- **Stats** show your current streak and weekly completion percentage

## Data Storage

Your habits are saved to `habits.json` in this folder. This file is human-readable, so you can:

- Back it up whenever you like
- Sync it with cloud storage (Dropbox, iCloud, etc.)
- Edit it manually if needed

## Managing the Service

```bash
# Stop the service and remove auto-start
./uninstall.sh

# Reinstall after uninstalling
./setup.sh

# View server logs
cat server.log
```

Your habit data (habits.json) is never deleted by these scripts.

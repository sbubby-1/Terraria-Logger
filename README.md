## Overview

This is a tool that complements world resetting in Terraria. Its provides
feedback upon resetting and automatically saves worlds that meet set criteria.

## Display

![Logger](https://github.com/user-attachments/assets/0ed39fdd-e0eb-42b9-8322-231c8f19521f)

The purpose of the display is to provide realtime feedback in order to improve
my pattern recognition with regards to world generation. As such, the display
window is kept as small as possible and only shows information that I believe to be
useful feedback for resetting. These are:

- Spawn position
- Dungeon position
- Pyramid item locations

The display is set to be above other windows, as I use it on a 2nd monitor with
other windows open. Its visibility can be toggled with Ctrl + Shift + H for
single-monitor usage.

## Saving Seeds

If desired, a relevant info about a seed can be saved. This can be done
manually through a hotkey (Ctrl + Shift + P), or automatically when certain
criteria are met. These criteria can be adjusted in Autosave.json.

Saved seeds are stored in a JSON format in a "Saved Seeds" folder, located in
Terraria's default folder.

## Hotkeys

Ctrl + Shift + M - Deletes the first .wld file found in the Worlds folder and
logs relevant info. This tool should be used alongside an AHK macro (to delete the
Player file and generate the next player/world), so it's easiest to include the
key combo within the AHK macro.

Ctrl + Shift + P - Saves the most recently analyzed world.

Ctrl + Shift + H - Toggles the visibility of the display.

## Compatibility

This tool is created for personal use, and as such will not be adapted to other
OS's, nor made compatible with older game versions (this tool is made for
1.4.4.9 .wld file structure).

I may update this for future versions of the game.

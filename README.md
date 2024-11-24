# Dump Me Weekly
Dump Me Weekly is a Python script for automatically saving tracks from Spotify's Disovery Weekly playlist into another playlist. It saves the user from losing the opportunity to discover new music before the playlist is updated.

## How To Use
1. Download this repository as `.zip` and unpack
2. Create and activate a python virtual environment and install `requirements.txt`
3. Edit `wrapper_script.sh` to your file paths (uses zsh) and run the script
### optional: use cron to automate
I have my crontab set to run the script every Sunday at 9pm: `0 21 * * 0 /pah/to/wrapper-script.sh`

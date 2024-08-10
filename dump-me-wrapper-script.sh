#!/bin/zsh

VENV_PATH="/path/to/venv/bin/activate"
SCRIPT_PATH="/path/to/dir/dump-me-weekly.py"

source $VENV_PATH

/path/to/venv/bin/python3 $SCRIPT_PATH

osascript -e 'display notification "discover weekly saved" with title "dump me weekly"'
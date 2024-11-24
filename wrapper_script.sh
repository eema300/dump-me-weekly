#!/bin/zsh

VENV_PATH="/path/to/env/bin/activate"
SCRIPT_PATH="/path/to/dump-me-weekly.py"

source $VENV_PATH

/path/to/env/bin/python3 $SCRIPT_PATH

osascript -e 'display notification "dump me weekly updated :)" with title "dumping....."'

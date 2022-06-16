#! /bin/bash
gunicorn --workers 1 --bind "0.0.0.0:5500" --error-logfile - --enable-stdio-inheritance --reload --keep-alive 5 --log-level "debug" "manage:app"

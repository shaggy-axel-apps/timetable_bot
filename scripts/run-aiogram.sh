#!/bin/bash

# Create Environment "Virtual Environment file path", "Deploy Flag file path"
VENV=./.venv

# Run Django
echo "Run Telegram Bot"
$VENV/bin/python src/manage.py runbot
echo "Telegram Bot Killed"

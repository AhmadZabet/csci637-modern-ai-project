"""Shared paths and JSON helpers."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# takes the path to a JSON file.
def read(path):
    # Read the file as UTF-8, accept an optional UTF-8 marker, and parse the JSON.
    return json.loads(path.read_text(encoding="utf-8-sig"))

#takes a destination path and a value to save.
def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def normalize(text):
    return " ".join(text.split())

#creates a key for comparing text.
def key(text):
    # Clean the spacing, then use casefold() to compare without regard to case
    return normalize(text).casefold()

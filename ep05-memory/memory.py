import json
from pathlib import Path

FILE = Path("memory.json")
TOOL_RULE = "Use the remember tool to save facts the user wants you to keep."


def remember(fact: str) -> str:
    """Save a fact about the user for future conversations.

    Args:
        fact: One short sentence about the user, like "The user likes tea."
    """
    FILE.write_text(json.dumps([*recall(), fact]))
    return "saved"


def recall() -> list:
    return json.loads(FILE.read_text()) if FILE.exists() else []

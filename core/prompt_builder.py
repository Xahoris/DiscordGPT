"""Build prompts for OpenAI API."""

from typing import List, Dict


def build_messages(conversation_history: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Build message list for OpenAI API.

    Args:
        conversation_history: List of messages with role and content

    Returns:
        Formatted message list ready for OpenAI API
    """
    return conversation_history


def validate_message_format(messages: List[Dict[str, str]]) -> bool:
    """
    Validate that messages follow OpenAI format.

    Args:
        messages: List of message dictionaries

    Returns:
        True if valid format, False otherwise
    """
    if not messages:
        return False

    for msg in messages:
        if "role" not in msg or "content" not in msg:
            return False
        if msg["role"] not in ["system", "user", "assistant"]:
            return False

    return True

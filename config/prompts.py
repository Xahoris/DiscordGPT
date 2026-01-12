"""System prompts and prompt templates."""

DEFAULT_SYSTEM_PROMPT = """You are a helpful AI assistant integrated into Discord. 
You provide clear, concise, and accurate responses to user questions.
Be friendly and professional in your interactions."""


def get_system_prompt() -> str:
    """Get the system prompt for conversations."""
    return DEFAULT_SYSTEM_PROMPT

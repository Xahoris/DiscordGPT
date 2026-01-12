"""Configuration settings for DiscordGPT."""

import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """Application settings loaded from environment variables."""

    def __init__(self):
        """Initialize settings from environment variables."""
        self.discord_token = os.getenv("DISCORD_TOKEN", "")
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.max_conversation_messages = int(
            os.getenv("MAX_CONVERSATION_MESSAGES", "20")
        )
        self.max_response_tokens = int(os.getenv("MAX_RESPONSE_TOKENS", "1000"))
        self.max_prompt_length = int(os.getenv("MAX_PROMPT_LENGTH", "2000"))
        self.rate_limit_per_user = int(os.getenv("RATE_LIMIT_PER_USER", "10"))

        # Validate required settings
        if not self.discord_token:
            raise ValueError("DISCORD_TOKEN not found in environment variables")
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")


def load_settings() -> Settings:
    """Load and validate settings from environment."""
    return Settings()

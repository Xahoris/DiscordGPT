"""OpenAI API client wrapper."""

from typing import Dict, List, Optional

from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion

from config.settings import Settings
from utils.logger import get_logger

logger = get_logger()


class OpenAIClient:
    """Wrapper for OpenAI API interactions."""

    def __init__(self, settings: Settings):
        self.settings = settings
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)

    async def get_chat_completion(
        self, messages: List[Dict[str, str]]
    ) -> Optional[str]:
        """
        Get a chat completion from OpenAI.

        Args:
            messages: List of messages in OpenAI format

        Returns:
            Assistant's response text or None if error
        """
        try:
            response: ChatCompletion = await self.client.chat.completions.create(
                model=self.settings.openai_model,
                messages=messages,
                max_tokens=self.settings.max_response_tokens,
            )

            if response.choices and len(response.choices) > 0:
                content = response.choices[0].message.content

                # Log token usage
                if response.usage:
                    logger.debug(
                        f"Token usage - Prompt: {response.usage.prompt_tokens}, "
                        f"Completion: {response.usage.completion_tokens}, "
                        f"Total: {response.usage.total_tokens}"
                    )

                return content
            else:
                logger.error("No choices in OpenAI response")
                return None

        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            return None

    async def close(self) -> None:
        """Close the OpenAI client."""
        await self.client.close()

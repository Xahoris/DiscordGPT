"""Main entry point for DiscordGPT bot."""

import asyncio
import os
import signal
import sys

from config.settings import load_settings
from bot_discord.client import create_bot
from utils.logger import get_logger, setup_logger


def main():
    """Main function to start the bot."""
    # Setup logging
    setup_logger()
    logger = get_logger()

    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    logger.info("Starting DiscordGPT...")

    try:
        # Load settings
        settings = load_settings()
        logger.info("Settings loaded successfully")

        # Create bot
        bot = create_bot(settings)
        logger.info("Bot created successfully")

        # Handle graceful shutdown
        def handle_shutdown(signum, frame):
            logger.info("Received shutdown signal, cleaning up...")
            asyncio.create_task(shutdown(bot))

        signal.signal(signal.SIGINT, handle_shutdown)
        signal.signal(signal.SIGTERM, handle_shutdown)

        # Start bot
        logger.info("Starting bot...")
        bot.run(settings.discord_token)

    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        sys.exit(1)


async def shutdown(bot):
    """Gracefully shutdown the bot."""
    logger = get_logger()
    logger.info("Shutting down bot...")

    try:
        if hasattr(bot, "openai_client"):
            await bot.openai_client.close()
            logger.info("OpenAI client closed")

        await bot.close()
        logger.info("Bot closed successfully")

    except Exception as e:
        logger.error(f"Error during shutdown: {e}")


if __name__ == "__main__":
    main()

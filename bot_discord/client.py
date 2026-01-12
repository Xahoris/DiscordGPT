"""Discord bot client and event handlers."""

import discord
from discord.ext import commands

from config.settings import Settings
from core.conversation import ConversationManager
from core.openai_client import OpenAIClient
from bot_discord.commands import setup_commands
from utils.logger import get_logger

logger = get_logger()


def create_bot(settings: Settings) -> commands.Bot:
    """
    Create and configure the Discord bot.

    Args:
        settings: Application settings

    Returns:
        Configured Discord bot instance
    """
    intents = discord.Intents.default()
    intents.message_content = True
    intents.dm_messages = True

    bot = commands.Bot(
        command_prefix="!",  # Not used, but required
        intents=intents,
        description="DiscordGPT - AI Assistant for Discord",
    )

    # Initialize components
    conversation_manager = ConversationManager(
        max_messages=settings.max_conversation_messages
    )
    openai_client = OpenAIClient(settings)

    # Event handlers
    @bot.event
    async def on_ready():
        """Called when the bot is ready."""
        logger.info(f"Bot is ready! Logged in as {bot.user}")
        logger.info(f"Bot ID: {bot.user.id}")
        logger.info("Registered commands:")
        for command in bot.pending_application_commands:
            logger.info(f"  /{command.name}")

    @bot.event
    async def on_application_command_error(
        ctx: discord.ApplicationContext, error: Exception
    ):
        """Handle command errors."""
        logger.error(f"Command error: {error}")
        if not ctx.response.is_done():
            await ctx.respond(
                "❌ An error occurred while processing your command.",
                ephemeral=True,
            )

    # Register commands
    setup_commands(bot, conversation_manager, openai_client, settings)

    # Store references for cleanup
    bot.conversation_manager = conversation_manager
    bot.openai_client = openai_client

    return bot

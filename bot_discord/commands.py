"""Discord bot commands."""

import discord
from discord import ApplicationContext, Option
from discord.ext import commands

from config.settings import Settings
from core.conversation import ConversationManager
from core.openai_client import OpenAIClient
from utils.logger import get_logger

logger = get_logger()


class DiscordCommands(commands.Cog):
    """Discord bot commands for GPT interactions."""

    def __init__(
        self,
        bot: commands.Bot,
        conversation_manager: ConversationManager,
        openai_client: OpenAIClient,
        settings: Settings,
    ):
        self.bot = bot
        self.conversation_manager = conversation_manager
        self.openai_client = openai_client
        self.settings = settings

    def _is_dm(self, ctx: ApplicationContext) -> bool:
        """Check if the command is used in a DM."""
        return isinstance(ctx.channel, discord.DMChannel)

    @discord.slash_command(name="gpt", description="Chat with GPT AI assistant")
    async def gpt(
        self,
        ctx: ApplicationContext,
        prompt: Option(str, "Your message to GPT", required=True),
    ):
        """Handle /gpt command to interact with AI."""
        # Check if DM only
        if not self._is_dm(ctx):
            await ctx.respond(
                "❌ This bot only works in Direct Messages. Please DM me!",
                ephemeral=True,
            )
            return

        # Validate prompt length
        if len(prompt) > self.settings.max_prompt_length:
            await ctx.respond(
                f"❌ Prompt too long! Maximum length is {self.settings.max_prompt_length} characters.",
                ephemeral=True,
            )
            return

        await ctx.defer()

        try:
            user_id = ctx.author.id
            logger.info(f"User {user_id} sent prompt: {prompt[:50]}...")

            # Add user message to conversation
            self.conversation_manager.add_message(user_id, "user", prompt)

            # Get conversation history
            messages = self.conversation_manager.get_messages(user_id)

            # Get AI response
            response = await self.openai_client.get_chat_completion(messages)

            if response:
                # Add assistant response to conversation
                self.conversation_manager.add_message(user_id, "assistant", response)

                # Send response to user
                await ctx.followup.send(response)
                logger.info(f"Sent response to user {user_id}")
            else:
                await ctx.followup.send(
                    "❌ Sorry, I encountered an error while processing your request. Please try again."
                )
                logger.error(f"Failed to get response for user {user_id}")

        except Exception as e:
            logger.error(f"Error in /gpt command: {e}")
            await ctx.followup.send(
                "❌ An unexpected error occurred. Please try again later."
            )

    @discord.slash_command(name="reset", description="Clear your conversation history")
    async def reset(self, ctx: ApplicationContext):
        """Handle /reset command to clear conversation history."""
        if not self._is_dm(ctx):
            await ctx.respond(
                "❌ This bot only works in Direct Messages. Please DM me!",
                ephemeral=True,
            )
            return

        try:
            user_id = ctx.author.id
            self.conversation_manager.reset_conversation(user_id)
            await ctx.respond("✅ Your conversation history has been cleared!")
            logger.info(f"Reset conversation for user {user_id}")

        except Exception as e:
            logger.error(f"Error in /reset command: {e}")
            await ctx.respond("❌ An error occurred while resetting. Please try again.")

    @discord.slash_command(name="help", description="Show available commands")
    async def help(self, ctx: ApplicationContext):
        """Handle /help command to display usage information."""
        help_text = """
**DiscordGPT Commands** 🤖

`/gpt <prompt>` - Chat with the AI assistant
Send any message or question to get an AI response.

`/reset` - Clear your conversation history
Start fresh with a new conversation.

`/usage` - View your conversation stats
See how many messages are in your current conversation.

`/help` - Show this help message

**Note:** This bot only works in Direct Messages (DMs).
"""
        await ctx.respond(help_text)

    @discord.slash_command(
        name="usage", description="View your conversation statistics"
    )
    async def usage(self, ctx: ApplicationContext):
        """Handle /usage command to show conversation stats."""
        if not self._is_dm(ctx):
            await ctx.respond(
                "❌ This bot only works in Direct Messages. Please DM me!",
                ephemeral=True,
            )
            return

        try:
            user_id = ctx.author.id
            message_count = self.conversation_manager.get_message_count(user_id)
            max_messages = self.settings.max_conversation_messages

            usage_text = f"""
**Conversation Statistics** 📊

Messages in history: {message_count}/{max_messages}
Model: {self.settings.openai_model}

Your conversation history is maintained across messages.
Use `/reset` to clear it.
"""
            await ctx.respond(usage_text)

        except Exception as e:
            logger.error(f"Error in /usage command: {e}")
            await ctx.respond(
                "❌ An error occurred while fetching usage. Please try again."
            )


def setup_commands(
    bot: commands.Bot,
    conversation_manager: ConversationManager,
    openai_client: OpenAIClient,
    settings: Settings,
) -> None:
    """Register commands with the bot."""
    bot.add_cog(DiscordCommands(bot, conversation_manager, openai_client, settings))

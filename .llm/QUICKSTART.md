# DiscordGPT - Quick Start Guide

## Step 1: Set Up Your Environment

1. **Copy the environment template:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` and add your credentials:**
   - Get Discord Bot Token from: https://discord.com/developers/applications
   - Get OpenAI API Key from: https://platform.openai.com/api-keys

   ```env
   DISCORD_TOKEN=your_actual_discord_bot_token
   OPENAI_API_KEY=your_actual_openai_api_key
   ```

## Step 2: Create Discord Bot

1. Go to https://discord.com/developers/applications
2. Click "New Application" → Name it
3. Go to "Bot" section:
   - Click "Add Bot"
   - Click "Reset Token" and copy the token
   - Enable these intents:
     - ✅ Message Content Intent
     - ✅ Direct Messages
4. Go to "OAuth2" > "URL Generator":
   - Scopes: `bot`, `applications.commands`
   - Bot Permissions: 
     - Send Messages
     - Read Message History
   - Copy the generated URL
5. Open the URL in browser to invite bot to your server

## Step 3: Run the Bot

```bash
# From project directory
uv run python bot.py
```

## Step 4: Test in Discord

1. Find your bot in Discord
2. Send it a Direct Message (DM)
3. Type `/gpt Hello!`
4. The bot should respond!

## Commands

- `/gpt <message>` - Chat with AI
- `/reset` - Clear conversation
- `/usage` - See stats
- `/help` - Show help

## Troubleshooting

**Bot doesn't respond:**
- Check `.env` file has correct tokens
- Make sure bot intents are enabled
- Verify you're in a DM, not a server channel

**"Application did not respond" error:**
- Check console logs for errors
- Verify OpenAI API key is valid
- Check your OpenAI account has credits

**Import errors:**
- Run `uv sync` to reinstall dependencies
- Check you're using Python 3.9+

## Next Steps

- Modify system prompt in `config/prompts.py`
- Adjust settings in `.env`
- Check logs in `logs/` directory for debugging

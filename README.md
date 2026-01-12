# DiscordGPT 🤖

A Discord bot that brings OpenAI's GPT capabilities to Discord Direct Messages.

## Features

- 💬 Private AI conversations via Discord DMs
- 🧠 Conversation memory with sliding window
- ⚡ Simple slash commands
- 🔒 DM-only for privacy
- 📊 Usage tracking

## Commands

- `/gpt <prompt>` - Chat with the AI assistant
- `/reset` - Clear your conversation history
- `/usage` - View your conversation statistics
- `/help` - Display help information

## Setup

### Prerequisites

- Python 3.9+
- Discord account
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd DiscordGPT
   ```

2. **Install dependencies with uv**
   ```bash
   uv sync
   ```

### Discord Bot Setup

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to "Bot" section and click "Add Bot"
4. Enable these Privileged Gateway Intents:
   - Message Content Intent
   - Direct Messages
5. Copy the bot token

6. Go to "OAuth2" > "URL Generator"
7. Select scopes:
   - `bot`
   - `applications.commands`
8. Select bot permissions:
   - Send Messages
   - Read Message History
9. Copy the generated URL and open it to invite the bot to your server

### Configuration

1. **Copy the example environment file**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` with your credentials**
   ```env
   DISCORD_TOKEN=your_discord_bot_token_here
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_MODEL=gpt-4o-mini
   ```

3. **Adjust settings as needed**
   - `MAX_CONVERSATION_MESSAGES`: Number of messages to keep in memory (default: 20)
   - `MAX_RESPONSE_TOKENS`: Maximum tokens in AI response (default: 1000)
   - `MAX_PROMPT_LENGTH`: Maximum characters in user prompt (default: 2000)

## Running the Bot

```bash
uv run python bot.py
```

Or activate the virtual environment:
```bash
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

python bot.py
```

## Usage

1. Send a DM to your bot on Discord
2. Use `/gpt` followed by your message
3. The bot will respond with AI-generated text
4. Your conversation history is maintained automatically
5. Use `/reset` to start a new conversation

## Project Structure

```
discordgpt/
├── bot.py                 # Main entry point
├── .env                   # Environment variables (create from .env.example)
├── config/
│   ├── settings.py        # Configuration management
│   └── prompts.py         # System prompts
├── core/
│   ├── conversation.py    # Conversation memory management
│   ├── prompt_builder.py  # Message formatting
│   └── openai_client.py   # OpenAI API wrapper
├── bot_discord/
│   ├── client.py          # Discord bot client
│   └── commands.py        # Slash commands
└── utils/
    └── logger.py          # Logging configuration
```

## Development

### Code Quality

```bash
# Format code
uv run ruff format .

# Check for issues
uv run ruff check .

# Fix auto-fixable issues
uv run ruff check . --fix
```

### Type Checking

```bash
# Initialize pyright
pyrefly init

# Check types
pyrefly check
```

## Limitations (Phase 1)

- DM-only interactions (no server channels)
- In-memory conversation storage (resets on restart)
- No long-term memory or embeddings
- Basic rate limiting

## Security Notes

- Never commit `.env` file
- Keep your Discord token and OpenAI API key secret
- Use environment variables for all sensitive data

## License

MIT

## Support

For issues or questions, please open an issue on GitHub.

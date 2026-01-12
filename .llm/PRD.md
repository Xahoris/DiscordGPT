# DiscordGPT -- Product Requirements Document (PRD)

## 1. Overview

**Project Name:** DiscordGPT\
**Type:** Discord Bot (Private Messages only -- Phase 1)\
**Technology:** Python, Discord API, OpenAI API\
**Deployment Target:** Local environment (prototype phase)

DiscordGPT is a Discord bot that allows users to interact with
OpenAI-powered conversational AI through Discord private messages (DMs).
The goal of Phase 1 is to deliver a clean, maintainable, and functional
prototype with a simple conversation memory system.

------------------------------------------------------------------------

## 2. Goals & Objectives

### Primary Goals

-   Enable private 1-on-1 conversations with an AI assistant via Discord
    DMs
-   Provide a ChatGPT-like experience inside Discord
-   Establish a clean technical foundation for future iterations

### Non-Goals (Phase 1)

-   Server/channel-based interactions
-   Long-term memory or embeddings
-   Monetization or analytics dashboards
-   Production-grade deployment

------------------------------------------------------------------------

## 3. Target Users

-   Developers
-   Technical users
-   Individuals wanting private AI assistance within Discord

------------------------------------------------------------------------

## 4. Functional Requirements

### 4.1 Supported Interaction Mode

-   Private Messages (DM) only
-   Bot must ignore or reject server messages

### 4.2 Commands

#### `/gpt`

-   Accepts a user prompt
-   Sends the prompt + conversation history to OpenAI
-   Returns the AI response to the user
-   Updates conversation memory

#### `/reset`

-   Clears the user's conversation memory
-   Resets to initial system prompt

#### `/help`

-   Displays available commands and usage instructions

#### `/usage` (optional Phase 1)

-   Displays approximate request or token usage

------------------------------------------------------------------------

## 5. Conversation Management (Level 1)

### Scope

-   Memory stored in RAM only
-   One conversation per user

### Rules

-   Fixed-size sliding window (e.g. last N messages)
-   FIFO removal when limit is exceeded
-   System prompt always preserved
-   Resettable via `/reset`

### Conversation Key

-   `user_id`

------------------------------------------------------------------------

## 6. Prompt Strategy

### System Prompt

-   Fixed prompt defining assistant behavior
-   Stored in configuration
-   Loaded at conversation initialization

### Message Format

Compatible with OpenAI Chat Completion schema: - `system` - `user` -
`assistant`

------------------------------------------------------------------------

## 7. Technical Stack

### Language

-   Python 3.11+

### Core Libraries

-   `py-cord`
-   `openai`
-   `python-dotenv`
-   `loguru`
-   `aiolimiter` (optional)

### External APIs

-   Discord API
-   OpenAI API

------------------------------------------------------------------------

## 8. Project Structure

    discordgpt/
    ├── bot.py
    ├── .env
    ├── requirements.txt
    ├── config/
    │   ├── settings.py
    │   └── prompts.py
    ├── core/
    │   ├── conversation.py
    │   ├── prompt_builder.py
    │   └── openai_client.py
    ├── discord/
    │   ├── client.py
    │   └── commands.py
    └── utils/
        └── logger.py

------------------------------------------------------------------------

## 9. Deployment (Phase 1)

-   Local execution only
-   Environment variables via `.env`
-   Single-process bot

Example:

``` bash
python bot.py
```

------------------------------------------------------------------------

## 10. Security & Limitations

-   Rate limiting per user
-   Max prompt length
-   Max tokens per response
-   Basic error handling for API failures

------------------------------------------------------------------------

## 11. Logging & Error Handling

-   Structured logging
-   Errors logged but not exposed to users
-   Graceful handling of OpenAI and Discord API errors

------------------------------------------------------------------------

## 12. Success Criteria

-   Bot responds correctly in DMs
-   Conversations persist during runtime
-   `/reset` reliably clears memory
-   Codebase is readable and extensible

------------------------------------------------------------------------

## 13. Future Considerations (Out of Scope)

-   Docker deployment
-   Server-based usage
-   Streaming responses
-   Long-term memory
-   Plugin/skill system

#!/usr/bin/env python
"""Test script for OpenAI API integration."""

import asyncio
import os

from dotenv import load_dotenv
from openai import AsyncOpenAI


async def test_openai():
    """Test OpenAI API with a simple prompt."""
    print("🧪 Testing OpenAI API...\n")

    # Load environment variables
    load_dotenv()

    # Get configuration from environment
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    max_tokens = int(os.getenv("MAX_RESPONSE_TOKENS", "1000"))

    if not api_key:
        print("✗ OPENAI_API_KEY not found in .env file")
        return

    print("✓ Environment variables loaded")
    print(f"  Model: {model}")
    print(f"  Max tokens: {max_tokens}\n")

    # Create OpenAI client
    try:
        client = AsyncOpenAI(api_key=api_key)
        print("✓ OpenAI client created\n")
    except Exception as e:
        print(f"✗ Failed to create OpenAI client: {e}")
        return

    # Test prompt
    prompt = "hello how are you"
    print(f"📝 Prompt: {prompt}\n")

    # Build messages
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": prompt},
    ]

    # Get response
    try:
        print("⏳ Waiting for response...\n")
        completion = await client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
        )

        if completion.choices and len(completion.choices) > 0:
            response = completion.choices[0].message.content
            print("✅ Success! Response received:\n")
            print("-" * 50)
            print(response)
            print("-" * 50)
            print(f"\n📊 Response length: {len(response)} characters")

            # Show token usage if available
            if completion.usage:
                print("📊 Token usage:")
                print(f"   Prompt tokens: {completion.usage.prompt_tokens}")
                print(f"   Completion tokens: {completion.usage.completion_tokens}")
                print(f"   Total tokens: {completion.usage.total_tokens}")
        else:
            print("✗ No response received from OpenAI")
            print("   Check your API key and internet connection")
            print("   Make sure your OpenAI account has credits")

    except Exception as e:
        print(f"✗ Error getting response: {e}")
        import traceback

        traceback.print_exc()
    finally:
        await client.close()
        print("\n✓ Client closed")


def main():
    """Main entry point."""
    asyncio.run(test_openai())


if __name__ == "__main__":
    main()

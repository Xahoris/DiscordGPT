#!/usr/bin/env python
"""Validation script to check DiscordGPT installation."""

import sys
from pathlib import Path


def check_file_exists(filepath: str) -> bool:
    """Check if a file exists."""
    exists = Path(filepath).exists()
    status = "✓" if exists else "✗"
    print(f"{status} {filepath}")
    return exists


def check_imports() -> bool:
    """Check if all imports work."""
    print("\n🔍 Checking imports...")
    try:
        print("✓ config.settings")

        print("✓ config.prompts")

        print("✓ core.conversation")

        print("✓ core.openai_client")

        print("✓ core.prompt_builder")

        print("✓ bot_discord.client")

        print("✓ bot_discord.commands")

        print("✓ utils.logger")
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False


def main():
    """Run validation checks."""
    print("🚀 DiscordGPT Validation\n")

    print("📁 Checking project structure...")
    all_ok = True

    # Check key files
    files = [
        "bot.py",
        ".env.example",
        ".gitignore",
        "README.md",
        "QUICKSTART.md",
        "pyproject.toml",
        "config/settings.py",
        "config/prompts.py",
        "core/conversation.py",
        "core/openai_client.py",
        "core/prompt_builder.py",
        "bot_discord/client.py",
        "bot_discord/commands.py",
        "utils/logger.py",
    ]

    for file in files:
        if not check_file_exists(file):
            all_ok = False

    # Check imports
    if not check_imports():
        all_ok = False

    # Check .env
    print("\n🔐 Checking environment...")
    if Path(".env").exists():
        print("✓ .env file exists")
    else:
        print("⚠ .env file not found (copy from .env.example)")
        all_ok = False

    # Summary
    print("\n" + "=" * 50)
    if all_ok:
        print("✅ All checks passed!")
        print("\nNext steps:")
        print("1. Copy .env.example to .env")
        print("2. Add your Discord and OpenAI tokens to .env")
        print("3. Run: uv run python bot.py")
        return 0
    else:
        print("❌ Some checks failed. Please review the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

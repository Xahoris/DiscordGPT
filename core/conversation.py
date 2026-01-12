"""Conversation management and memory storage."""

from collections import deque
from typing import Dict, List

from config.prompts import get_system_prompt


class Message:
    """Represents a single message in a conversation."""

    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def to_dict(self) -> Dict[str, str]:
        """Convert message to OpenAI API format."""
        return {"role": self.role, "content": self.content}


class Conversation:
    """Manages a single user's conversation history."""

    def __init__(self, max_messages: int = 20):
        self.max_messages = max_messages
        self.system_prompt = get_system_prompt()
        self.messages: deque = deque(maxlen=max_messages)

    def add_message(self, role: str, content: str) -> None:
        """Add a message to the conversation."""
        self.messages.append(Message(role, content))

    def get_messages(self) -> List[Dict[str, str]]:
        """Get all messages including system prompt in OpenAI format."""
        result = [{"role": "system", "content": self.system_prompt}]
        result.extend([msg.to_dict() for msg in self.messages])
        return result

    def reset(self) -> None:
        """Clear all messages except system prompt."""
        self.messages.clear()

    def message_count(self) -> int:
        """Get the number of messages (excluding system prompt)."""
        return len(self.messages)


class ConversationManager:
    """Manages conversations for all users."""

    def __init__(self, max_messages: int = 20):
        self.max_messages = max_messages
        self.conversations: Dict[int, Conversation] = {}

    def get_conversation(self, user_id: int) -> Conversation:
        """Get or create a conversation for a user."""
        if user_id not in self.conversations:
            self.conversations[user_id] = Conversation(self.max_messages)
        return self.conversations[user_id]

    def add_message(self, user_id: int, role: str, content: str) -> None:
        """Add a message to a user's conversation."""
        conversation = self.get_conversation(user_id)
        conversation.add_message(role, content)

    def get_messages(self, user_id: int) -> List[Dict[str, str]]:
        """Get all messages for a user in OpenAI format."""
        conversation = self.get_conversation(user_id)
        return conversation.get_messages()

    def reset_conversation(self, user_id: int) -> None:
        """Reset a user's conversation."""
        if user_id in self.conversations:
            self.conversations[user_id].reset()

    def get_message_count(self, user_id: int) -> int:
        """Get the number of messages for a user."""
        if user_id not in self.conversations:
            return 0
        return self.conversations[user_id].message_count()

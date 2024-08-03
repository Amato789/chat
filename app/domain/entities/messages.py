from dataclasses import dataclass, field

from app.domain.entities.base import BaseEntity
from app.domain.values.messages import Text, Title


@dataclass
class Message(BaseEntity):
    text: Text


@dataclass
class Chat(BaseEntity):
    title: Title
    messages: list[Message] = field(
        default_factory=list,
        kw_only=True,
    )

    def add_message(self, message: Message):
        self.messages.append(message)

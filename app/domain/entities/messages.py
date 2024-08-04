from dataclasses import dataclass, field

from app.domain.entities.base import BaseEntity
from app.domain.events.messages import NewMessageReceivedEvent, NewChatCreated
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

    @classmethod
    def create_chat(cls, title: Title) -> 'Chat':
        new_chat = cls(title=title)
        new_chat.register_event(NewChatCreated(chat_oid=new_chat.oid, chat_title=new_chat.title.as_generic_type()))

    def add_message(self, message: Message):
        self.messages.append(message)
        self.register_event(NewMessageReceivedEvent(
            message_text=message.text.as_generic_type(),
            chat_oid=self.oid,
            message_oid=message.oid,
        ))

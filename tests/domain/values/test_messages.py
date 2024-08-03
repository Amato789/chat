import pytest

from app.domain.entities.messages import Message, Chat
from app.domain.exceptions.messages import TextTooLongException
from app.domain.values.messages import Text, Title


def test_create_message_success():
    text = Text('Sample text bla bla')
    message = Message(text=text)

    assert message.text == text


def test_create_message_text_too_long():
    with pytest.raises(TextTooLongException):
        text = Text('bla' * 100)


def test_create_chat_success():
    title = Title('title bla bla')
    chat = Chat(title=title)

    assert chat.title == title
    assert not chat.messages


def test_create_chat_title_too_long():
    with pytest.raises(TextTooLongException):
        title = Title('title bla bla' * 200)


def test_add_message_to_chat():
    text = Text('Sample text bla bla')
    message = Message(text=text)
    title = Title('title bla bla')
    chat = Chat(title=title)
    chat.add_message(message=message)

    assert message in chat.messages

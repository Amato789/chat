import pytest

from app.domain.entities.messages import Message, Chat
from app.domain.events.messages import NewMessageReceivedEvent
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


def test_new_message_event():
    text = Text('Sample text bla bla')
    message = Message(text=text)
    title = Title('title bla bla')
    chat = Chat(title=title)
    chat.add_message(message=message)
    events = chat.pull_events()
    pulled_events = chat.pull_events()

    assert not pulled_events, pulled_events
    assert len(events) == 1, events

    new_event = events[0]

    assert isinstance(new_event, NewMessageReceivedEvent), new_event
    assert new_event.message_oid == message.oid
    assert new_event.message_text == message.text.as_generic_type()
    assert new_event.chat_oid == chat.oid

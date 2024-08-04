from pytest import fixture

from app.infra.repositories.messages import BaseChatRepository, MemoryChatRepository
from app.logic import init_mediator
from app.logic.mediator import Mediator


@fixture(scope='package')
def chat_repository() -> MemoryChatRepository:
    repository = MemoryChatRepository()
    return repository


@fixture(scope='package')
def mediator(chat_repository: MemoryChatRepository) -> Mediator:
    mediator = Mediator()
    init_mediator(mediator=mediator, chat_repository=chat_repository)

    return mediator


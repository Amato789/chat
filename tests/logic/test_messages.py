import pytest

from app.domain.entities.messages import Chat
from app.infra.repositories.messages import BaseChatRepository, MemoryChatRepository
from app.logic.commands.messages import CreateChatCommand

from app.logic.mediator import Mediator


# @pytest.mark.asyncio
# async def test_create_chat_command_success(chat_repository: BaseChatRepository, mediator: Mediator):
#     # TODO
#     chat: Chat = (await mediator.handle_command(CreateChatCommand(title='gigaTitle')))[0]
#
#     assert chat_repository.check_chat_exist_by_title(title=chat.title.as_generic_type())

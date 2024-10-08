from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar, Any

from app.domain.events.base import BaseEvent

ET = TypeVar(name='ET', bound=BaseEvent)
ER = TypeVar(name='ER', bound=Any)


@dataclass
class EventHandler(ABC, Generic[ET, ER]):
    def handle(self, event: ET) -> ER:
        ...

from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from uuid import uuid4, UUID


@dataclass
class BaseEvent(ABC):
    event_id: UUID = field(default_factory=uuid4, kw_only=True)

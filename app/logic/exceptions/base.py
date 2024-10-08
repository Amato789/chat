from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class LogicException(ApplicationException):
    @property
    def message(self):
        return 'An error occurred in processing the request'

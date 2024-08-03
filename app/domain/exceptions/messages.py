from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class TextTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f'Too long text "{self.text[:255]}"'

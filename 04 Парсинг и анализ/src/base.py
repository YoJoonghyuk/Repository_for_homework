from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    _next: Optional[Handler] = None

    def set_next(self, handler: Handler) -> Handler:
        self._next = handler
        return handler

    @abstractmethod
    def handle(self, data: Any) -> Any:
        if self._next:
            return self._next.handle(data)
        return data

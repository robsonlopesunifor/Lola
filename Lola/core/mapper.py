from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Generic
from typing import TypeVar

T = TypeVar("T")


class Mapper(Generic[T], ABC):
    @staticmethod
    @abstractmethod
    def to_dto(t: T) -> Any:
        raise NotImplementedError()

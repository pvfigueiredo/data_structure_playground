from abc import ABC, abstractmethod


class iLinkedList(ABC):
    @abstractmethod
    def __init__(self, data=None) -> None:
        pass

    @abstractmethod
    def add(self, data: any):
        pass

    @abstractmethod
    def remove(self, index: int):
        pass
    
    @abstractmethod
    def insert(self, index: int, data: any):
        pass
    
    @abstractmethod
    def puts(self):
        pass

    @abstractmethod
    def get_by_index(self, index: int):
        pass

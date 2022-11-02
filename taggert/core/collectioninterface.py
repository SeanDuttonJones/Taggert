class ICollection:

    def add(self, object: object) -> None:
        pass

    def add_all(self, objects: list) -> None:
        pass

    def clear(self) -> None:
        pass

    def contains(self, object: object) -> bool:
        pass

    def contains_all(self, objects: list) -> bool:
        pass

    def is_empty(self) -> bool:
        pass

    def remove(self, object: object) -> None:
        pass

    def remove_all(self, objects: list) -> None:
        pass

    def size(self) -> int:
        pass

    def matching(self, collection_filter) -> object:
        pass

    def list(self) -> list:
        pass

class ICollectionFilter:

    def accept(object: object) -> bool:
        pass
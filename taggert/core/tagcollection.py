from taggert.core.collectioninterface import ICollection

class TagCollection(ICollection):

    def __init__(self):
        self.index = {}
        self.reversed_index = {}

    # Modifying the behaviour of this function may modify the 
    # behaviour of the add_all() function as the add_all()
    # function relies on this.
    def add(self, tag: object) -> None:
        tag_value = tag.get_value()
        if tag_value not in self.index:
            self.index[tag_value] = []

        self.index[tag_value].append(tag)

        tag_location = tag.get_location().get_path()
        if tag_location not in self.reversed_index:
            self.reversed_index[tag_location] = []

        self.reversed_index[tag_location].append(tag)

    def add_all(self, tags: list) -> None:
        for tag in tags:
            self.add(tag)

    def clear(self) -> None:
        self.index = {}
        self.reversed_index = {}

    def contains(self, tag: object) -> bool:
        return tag.get_value() in self.index

    def contains_all(self, tags: list) -> bool:
        for tag in tags:
            if tag.get_value() not in self.index:
                return False
        
        return True

    def is_empty(self) -> bool:
        return bool(self.index) # Empty dictionaries evaluate to False

    # Modifying the behaviour of this function may modify the 
    # behaviour of the remove_all() function as the remove_all()
    # function relies on this.
    def remove(self, tag: object) -> None:
        tags = self.reversed_index.pop(tag.get_location().get_path(), None)

        if tags:
            for tag in tags:
                self.index[tag.get_value()].remove(tag.get_location().get_path())

                if len(self.index[tag.get_value()]) == 0:
                    self.index.pop(tag.get_value(), None)

    def remove_all(self, tags: list) -> None:
        for tag in tags:
            self.remove(tag)

    def size(self) -> int:
        return len(self.index)

    def matching(self, collection_filter) -> object:
        tags = []
        for value in self.index.values():
            tags.extend(value)

        tags = list(set(tags))

        return [t for t in tags if collection_filter.accept(t)]

    def list(self) -> list:
        return list(self.index.keys())
import os

class FileTreeNode:

    def __init__(self, path, mtime, size, is_directory):
        self.path = path
        self.mtime = mtime
        self.size = size
        self.is_dir = is_directory

        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        if(child in self.children):
            self.children.remove(child)

    def print(self, level=0, pretty_print=True):
        name = self.path
        if(pretty_print):
            name = os.path.basename(name)
        
        print("\t" * level, name)
        
        for child in self.children:
            child.print(level + 1, pretty_print)

    def to_dict(self):
        json = {
            "path": self.path,
            "mtime": self.mtime,
            "size": self.size,
            "is_directory": self.is_dir
        }

        children = []
        for child in self.children:
            children.append(child.to_dict())

        json["children"] = children
        return json

    def list_nodes(self, filter):
        nodes = []
        if(filter(self)):
            nodes.append(self)

        for child in self.children:
            nodes.extend(child.list_nodes(filter))

        return nodes

    def get_path(self):
        return self.path

    def get_mtime(self):
        return self.mtime

    def get_size(self):
        return self.size

    def is_directory(self):
        return self.is_dir

    def get_children(self):
        return self.children
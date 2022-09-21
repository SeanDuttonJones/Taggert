from taggert.diff.filetreenode import FileTreeNode
import os
import json

class FileTree:

    def __init__(self, root):
        self.root_dir = root
        self.root_node = None

    def _build(self, root):
        root_path = root
        root_mtime = os.path.getmtime(root)
        root_size = os.path.getsize(root)
        root_is_dir = os.path.isdir(root)
        root_node = FileTreeNode(root_path, root_mtime, root_size, root_is_dir)

        dirs = [os.path.join(root, d) for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
        files = [os.path.join(root, f) for f in os.listdir(root) if not os.path.isdir(os.path.join(root, f))]

        for file in files:
            child_name = file
            child_mtime = os.path.getmtime(file)
            child_size = os.path.getsize(file)
            child_is_dir = False
            child_node = FileTreeNode(child_name, child_mtime, child_size, child_is_dir)

            root_node.add_child(child_node)

        for dir in dirs:
            root_node.add_child(self._build(dir))

        return root_node

    def build(self):
        self.root_node = self._build(self.root_dir)
        return self.root_node

    def print(self, pretty_print=True):
        if(self.root_node == None):
            print("No tree available. Please build a tree before printing.")
            return False

        self.root_node.print(level = 0, pretty_print=pretty_print)

    def save(self, path, filename):
        if(self.root_node == None):
            print("No tree available. Please build a tree before saving.")
            return False

        with open(os.path.join(path, filename), "w") as f:
            f.write(json.dumps(self.root_node.to_dict()))

    def _load(self, tree_dict):
        root_path = tree_dict["path"]
        root_mtime = tree_dict["mtime"]
        root_size = tree_dict["size"]
        root_is_dir = tree_dict["is_directory"]
        root_node = FileTreeNode(root_path, root_mtime, root_size, root_is_dir)

        dirs = [d for d in tree_dict["children"] if d["is_directory"]]
        files = [f for f in tree_dict["children"] if not f["is_directory"]]

        for file in files:
            child_name = file["path"]
            child_mtime = file["mtime"]
            child_size = file["size"]
            child_is_dir = False
            child_node = FileTreeNode(child_name, child_mtime, child_size, child_is_dir)

            root_node.add_child(child_node)

        for dir in dirs:
            root_node.add_child(self._load(dir))

        return root_node

    def load(self, path):
        tree_dict = {}
        with open(path, "r") as f:
            tree_dict = json.loads(f.read())

        self.root_node = self._load(tree_dict)
        return self.root_node

    def list_file_nodes(self):
        return self.root_node.list_nodes(lambda x: not x.is_directory())

    def list_directory_nodes(self):
        return self.root_node.list_nodes(lambda x: x.is_directory())

    def list_nodes(self, filter):
        return self.root_node.list_nodes(filter)

    def get_root(self):
        if(self.root_node):
            return self.root_node

        return None
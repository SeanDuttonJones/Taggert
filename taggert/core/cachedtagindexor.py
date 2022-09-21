from taggert.diff.filetree import FileTree
from taggert.core.tagextractor import TagExtractor

import appdirs

import hashlib
import os

class CachedTagIndexor:

    def __init__(self, tag_index):
        self.tag_index = tag_index
        self.cache_dir = appdirs.user_cache_dir("Taggert", False)

    def _hash(self, value):
        return hashlib.sha1(value.encode("UTF-8")).hexdigest()

    def _cache(self, tree):
        root_path = tree.get_root().get_path()
        tree.save(self.cache_dir, self._hash(root_path))

    def _load_cache(self, root):
        cache_file = os.path.join(self.cache_dir, self._hash(root))
        if(not os.path.isfile(cache_file)):
            return None

        file_tree = FileTree(root)
        file_tree.load(cache_file)

        return file_tree

    def _py_file_resolver(self, file_tree_node):
        file_name = os.path.basename(file_tree_node.get_path())
        if(not file_tree_node.is_directory() and file_name.endswith(".py")):
            return True

    def _diff(self, old_tree, new_tree):
        old_nodes = old_tree.list_nodes(self._py_file_resolver)
        current_nodes = new_tree.list_nodes(self._py_file_resolver)

        old_file_paths = [n.get_path() for n in old_nodes]
        current_file_paths = [n.get_path() for n in current_nodes]

        deleted_files = list(set(old_file_paths) - set(current_file_paths))
        added_files = list(set(current_file_paths) - set(old_file_paths))
        modified_files = []

        for file in set.intersection(set(old_file_paths), set(current_file_paths)):
            old_i = old_file_paths.index(file)
            current_i = current_file_paths.index(file)

            if(old_nodes[old_i].get_mtime() < current_nodes[current_i].get_mtime()):
                modified_files.append(file)

        return (deleted_files, added_files, modified_files)

    def index(self, root):
        new_tree = FileTree(root)
        new_tree.build()

        tag_extractor = TagExtractor()
        files = []

        old_tree = self._load_cache(root)
        if(old_tree):
            d_files, a_files, m_files = self._diff(old_tree, new_tree)

            for d_file in d_files:
                self.tag_index.remove(d_file)

            files = a_files + m_files
        else:
            files = [n.get_path() for n in new_tree.list_nodes(self._py_file_resolver)]

        for file in files:
            with open(file, "r") as f:
                code = f.read()
                tags = tag_extractor.parse(code)

                if(tags):
                    for tag in tags:
                        self.tag_index.add(tag.lower(), file)

        self._cache(new_tree)

    def clear_cache(self):
        cache_files = os.listdir(self.cache_dir)
        for file in cache_files:
            os.remove(os.path.join(self.cache_dir, file))
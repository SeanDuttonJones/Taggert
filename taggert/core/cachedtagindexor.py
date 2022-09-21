from taggert.diff.filetree import FileTree

import taggert
import hashlib
import os

class CachedTagIndexor:

    def __init__(self, tag_index):
        self.tag_index = tag_index
        self.old_tree = None
        self.new_tree = None

    def _hash(self, value):
        return hashlib.sha1(value.encode("UTF-8")).hexdigest()

    def _cache(self):
        pass

    def _load_cache(self, root) -> bool:
        cache_dir = os.path.join(os.path.dirname(os.getcwd()), "/__cache__")
        print(cache_dir)
        if(not os.path.isdir(cache_dir)):
            os.mkdir(cache_dir)

        cache_file = os.path.join(cache_dir, self._hash(root))
        if(not os.path.isfile(cache_file)):
            return False

        file_tree = FileTree(root)
        file_tree.load(cache_file)

        self.old_tree = file_tree
        return True

    def index(self, root):
        print(self._load_cache(root))

    def clear_cache(self):
        pass
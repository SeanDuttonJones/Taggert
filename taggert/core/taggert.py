from taggert.core.filescanner import FileScanner
from taggert.core.tagextractor import TagExtractor
from taggert.core.tagindex import TagIndex
from taggert.core.cachedtagindexor import CachedTagIndexor

import os

class Taggert:
    
    def __init__(self):
        self.tag_index = TagIndex()

    def index(self):
        tag_indexor = CachedTagIndexor(self.tag_index)
        # tag_indexor.clear_cache()
        tag_indexor.index(os.path.join(os.getcwd(), "taggert"))

    def search(self, tag):
        self.index()
        return self.tag_index.find(tag)

    def list(self):
        self.index()
        return self.tag_index.listTags()
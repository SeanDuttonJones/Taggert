from TagIndex import TagIndex

class Taggert():
    
    def __init__(self):
        self.tag_index = TagIndex()
        pass

    def search(self, tag):
        return self.tag_index.find(tag)

    def list(self):
        return self.tag_index.listTags()
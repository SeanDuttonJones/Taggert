class TagIndex:

    def __init__(self):
        self.index = {}
        self.inverse_index = {}

    def add(self, tag, value):
        if(tag not in self.index):
            self.index[tag] = []

        self.index[tag].append(value)

        if(value not in self.inverse_index):
            self.inverse_index[value] = []
        
        self.inverse_index[value].append(tag)

    def remove(self, value):
        tags = self.inverse_index.pop(value, None)

        if(tags):
            for tag in tags:
                self.index[tag].remove(value)
                
                if(len(self.index[tag]) == 0):
                    self.index.pop(tag, None)

    def find(self, tag):
        if(tag not in self.index):
            return []

        return self.index[tag]

    def listTags(self):
        return list(self.index.keys())
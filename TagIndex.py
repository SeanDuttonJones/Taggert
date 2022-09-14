class TagIndex:

    def __init__(self):
        self.index = {}
        self.inverse_index = {}

    def add_value(self, tag, value):
        if(tag not in self.index):
            self.index[tag] = []

        self.index[tag].append(value)

        if(value not in self.inverse_index):
            self.inverse_index[value] = []
        
        self.inverse_index[value].append(tag)

    def remove_value(self, value):
        tags = self.inverse_index.pop(value, None)

        for tag in tags:
            self.index[tag].remove(value)
            
            if(len(self.index[tag]) == 0):
                self.index.pop(tag, None)

    def find(self, tag):
        if(tag not in self.index):
            return None

        return self.index[tag]
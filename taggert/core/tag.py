class Tag:

    def __init__(self, value, file):
        self.value = value
        self.location = file

    def get_value(self):
        return self.value

    def get_location(self):
        return self.location
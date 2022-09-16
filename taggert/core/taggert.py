from taggert.core.filescanner import FileScanner
from taggert.core.tagextractor import TagExtractor
from taggert.core.tagindex import TagIndex

class Taggert():
    
    def __init__(self):
        self.tag_index = TagIndex()

    def index(self):
        file_scanner = FileScanner("/Users/seanduttonjones/Documents/Work/Development/Python/Taggert/")
        tag_extractor = TagExtractor()

        python_files = file_scanner.scan([".py"])

        for file in python_files:
            with open(file, "r") as f:
                code = f.read()
                tags = tag_extractor.parse(code)
                
                if(tags == None):
                    continue

                for tag in tags:
                    self.tag_index.add(tag.lower(), file)

    def search(self, tag):
        self.index()
        return self.tag_index.find(tag)

    def list(self):
        self.index()
        return self.tag_index.listTags()
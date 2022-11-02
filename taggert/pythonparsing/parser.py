class IParser:

    def parse():
        pass

class PurePythonParser(IParser):

    def parse(self, file_path: str):
        print("Parsing Pure Python...")

class JupyterParser(IParser):

    def parse(self, file_path: str):
        print("Parsing Jupyter Notebook...")
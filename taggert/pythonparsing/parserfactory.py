from pythonparsing.parser import PurePythonParser, JupyterParser

class ParserFactory:

    def create_parser(self, file_extension):
        if file_extension == ".py":
            return PurePythonParser()

        elif file_extension == ".ipynb":
            return JupyterParser()

        return None
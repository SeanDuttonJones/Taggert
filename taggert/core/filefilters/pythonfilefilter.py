from taggert.core.filefilters.filefilter import FileFilter

class PythonFileFilter(FileFilter):

    def accept(self, file):
        if file.get_extension() == ".py":
            return True

        return False
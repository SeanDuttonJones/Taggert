import ctypes
import os

__tags__ = ["sean", "jack"]

class FileScanner:

    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.files = []

    def _file_has_hidden_attribute(self, path):
        try:
            attributes = ctypes.windll.kernel32.GetFileAttributesW(unicode(path))
            assert attributes != -1
            result = bool(attributes & 2)
        except (AttributeError, AssertionError):
            result = False

        return result

    def _is_file_hidden(self, path):
        name = os.path.basename(os.path.abspath(path))

        return name.startswith(".") or self._file_has_hidden_attribute(path)

    def scan(self, file_extensions = [""]):
        files = []

        directories = []
        directories.append(self.root_dir)

        while(len(directories) > 0):
            current_dir = directories.pop(0)
            
            for filename in os.listdir(current_dir):
                f = os.path.join(current_dir, filename)

                if(os.path.isdir(f) and not self._is_file_hidden(f)):
                    directories.append(f)
                    continue

                if(os.path.isfile(f) and f.endswith(tuple(file_extensions))):
                    files.append(f)

        return files

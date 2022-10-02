import ctypes
import hashlib
import os
import platform

class File:

    def __init__(self, pathname: str):
        if pathname is None:
            raise TypeError(f"pathname cannot be {None}.")
        elif type(pathname) != str:
            raise TypeError(f"pathname must be type str. {type(pathname)} was given instead.")

        self.pathname = pathname

    def get_name(self):
        return os.path.basename(self.pathname)

    def get_extension(self):
        return os.path.splitext(self.pathname)[-1]

    def get_parent(self):
        return os.path.dirname(self.pathname)

    def get_path(self):
        return self.pathname

    def get_size(self):
        if os.path.isdir(self.pathname):
            size = 0

            for path, dirs, files in os.walk(self.pathname):
                for f in files:
                    size += os.stat(os.path.join(path, f)).st_size

            return size

        return os.stat(self.pathname).st_size

    def exists(self):
        return os.path.exists(self.pathname)

    def hash(self):
        return hashlib.sha1(self.pathname.encode("UTF-8")).hexdigest()

    def is_directory(self):
        return os.path.isdir(self.pathname)

    def is_file(self):
        return os.path.isfile(self.pathname)

    def __is_hidden_windows(self):
        try:
            attributes = ctypes.windll.kernel32.GetFileAttributesW(self.pathname)
            assert attributes != -1
            result = bool(attributes & 2)
        except (AttributeError, AssertionError):
            result = False

        return result

    def __is_hidden_unix(self):
        filename = os.path.basename(self.pathname)
        return filename.startswith(".")

    def is_hidden(self):
        if platform.system() == "Windows":
            return self.__is_hidden_windows()

        return self.__is_hidden_unix()

    def last_modified(self):
        return os.stat(self.pathname).st_mtime

    def created(self):
        return os.stat(self.pathname).st_ctime

    def list(self, file_filter = None):
        if file_filter is None:
            return os.listdir(self.pathname)

        return [f for f in os.listdir(self.pathname) if file_filter.accept(File(os.path.join(self.pathname, f)))]

    def list_files(self):
        return [f for f in os.listdir(self.pathname) if os.path.isfile(os.path.join(self.pathname, f))]

    def list_directories(self):
        return [f for f in os.listdir(self.pathname) if os.path.isdir(os.path.join(self.pathname, f))]
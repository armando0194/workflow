from pathlib import Path
from ..enums import ProgrammingLanguage
from file import File

class Project():
     
    def __init__(self, id, name, path):
        """Constructor

        Args:
            id (int): id of the project
            name (str): name of the project
            path (str): path to the project
        """
        self.id = id
        self.name = name
        self.path = path
        self._files = {}

    @property
    def files(self):
        """ Returns the files associated to the
        project

        Returns:
            dict<str, File>: dictionary with files
        """
        self.update_files()
        return self._files

    @files.setter
    def files(self, value):
        """Setter

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
        """
        if isinstance(value, dict):
            raise TypeError("Files must be a dict")

        self._files = value

    def get_file(self, name: str):
        """Given a name, returns a file object

        Args:
            name (str): name of the file

        Returns:
            File: file object
        """
        return self._files[name]

    def get_current_files(self):
        """Traverses the project directory and generates
        a dict<str, File> with programming files(.cs, .java and .py)

        Returns:
            dict<str, File>: dictionary with programming files 
                             associated to the project
        """
        files = {}
        for file_type in ProgrammingLanguage:
            for path in Path(self.path).glob('**/*{}'.format(file_type.value)):
                name = f"{path}".split('/')[-1]
                files[name] = File(name, file_type, path)

        return files

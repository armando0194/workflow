from datetime import datetime


class File():
    def __init__(self, name: str, file_type: ProgrammingLanguage, path: str):
        """Constructor

        Args:
            name (str): name of the file
            file_type (ProgrammingLanguage): file extension
            path (str): file path
        """
        self.name = name
        self._path = path
        self._file_type = file_type
        self._last_analyzed = None
        self._todos = None

    @property
    def path(self):
        """Path of the file

        Returns:
            str: path to file
        """
        return self._path

    @property
    def file_type(self):
        """File type of the file see enums.ProgrammingLanguage
        to see supported file extensions

        Returns:
            ProgrammingLangauge: file type
        """
        return self._file_type

    @property
    def last_analyzed(self):
        """Datetime of the last time this file was analyzed
        by the system.  

        Returns:
            datetime: file last modified datetime
        """
        return self._last_analyzed

    @property
    def todos(self):
        """Todos associated with the file

        Returns:
            dict<str, Todo>: dictionary with todos
        """
        return self._todos

    @last_analyzed.setter
    def last_analyzed(self, value: datetime):
        """Setter for last analyzed property

        Args:
            value (datetime): new date value

        Raises:
            TypeError: the property must be datetime
        """
        if isinstance(value, datetime):
            raise TypeError("last_analyzed must be a datetime")

        self._last_analyzed = value

    @todos.setter
    def todos(self, value: dict):
        """Setter for todos property

        Args:
            value (dict<str, Todo>): new todos value

        Raises:
            TypeError: the property must be a dict
        """
        if isinstance(value, dict):
            raise TypeError("todos must be a dict")

        self._todos = value

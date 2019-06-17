import json
import glob
import os
import configparser

from enum import Enum
from sqlitedict import SqliteDict
from todoist import Todoist
from datetime import datetime
from pathlib import Path


class ProgrammingLanguage(Enum): 
    """ Enumerator class that represent the different 
    programming languages that can be parsed
    """
    java = ".java"
    python = ".py"

class File():
    def __init__(self, name: str, file_type: ProgrammingLanguage, path: str):
        self.name = name
        self._path = path
        self._file_type = file_type
        self._last_analyzed = None
        self._todos = None

    @property
    def path(self):
        return self._path

    @property
    def file_type(self):
        return self._file_type

    @property
    def last_analyzed(self):
        return self._last_analyzed

    @property
    def todos(self):
        return self._todos

    @last_analyzed.setter
    def last_analyzed(self, value: datetime):
        if isinstance(value, datetime):
            raise TypeError("last_analyzed must be a datetime")

        self._last_analyzed = value

    @todos.setter
    def todos(self, value: dict):
        if isinstance(value, dict):
            raise TypeError("todos must be a dict")

        self._todos = value


class Project():

    def __init__(self, id, name, path):
        self.id = id
        self.name = name
        self.path = path
        self._files = {}
    
    @property
    def files(self):
        self.update_files()
        return self._files

    @files.setter
    def files(self, value):
        if isinstance(value, dict):
            raise TypeError("files must be a dict")

        self._files = value

    def get_file(self, name: str):
        return self._files[name]

    def get_current_files(self):
        files = {}
        for file_type in ProgrammingLanguage:
            for path in Path(self.path).glob('**/*{}'.format(file_type.value)):                
                name = f"{path}".split('/')[-1]
                files[name] = File(name, file_type, path)
        
        return files


class ProjectManager():

    def __init__(self):
        self.projects = self.read_projects()
        print(self.projects)

    @property
    def projects(self):
        return self._projects

    @projects.setter
    def projects(self, value):
        self._projects = value

    def get_project(self, name):
        return self.projects[name]

    def read_projects(self):
        return SqliteDict('./project.sqlite', autocommit=True)

    def project_exists(self, name):
        return name in self.projects

    def create_project(self, name: str, id: int, path: str):
        self.projects[name] = Project(id, name, path)
        self.projects.commit()

    def remove_project(self, name: str):
        del self.projects[name]

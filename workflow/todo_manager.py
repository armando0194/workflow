import tokenize
import io
import re

from todoist import Todoist
from project import ProgrammingLanguage
from comment_parser import comment_parser

class Todo():
    def __init__(self, id: int, desc: str, priority: int):
        self._id = id
        self.desc = desc
        self.priority = priority
    
    @property
    def id(self):
        return self._id

class TodoManager():

    TODO_COMMENT = "TODO"
    TODO_PATTERN = r"TODO!*"
    TODO_OFFSET = len(TODO_COMMENT)
    PRIORITY_CHAR = '!'
    MIME_JAVA = "text/x-java-source"

    def __init__(self, api_key: str, project_id: int):
        self.project_id = project_id
        self.todoist = Todoist(api_key)

    def get_todos(self, path: str, file_type: ProgrammingLanguage):
        if file_type == ProgrammingLanguage.python:
            self.get_todos_python(path)
        elif file_type == ProgrammingLanguage.java:
            self.get_todos_java(path)
        else:
            raise Exception(path.split('.')[-1] + " not supported")

    def get_priority(self, line: str):
        priotity = re.findall(self.TODO_PATTERN, line)
        return priotity[0].count(self.PRIORITY_CHAR) if priotity else 1

    def get_todos_python(self, path: str):
        buf = open(path, "r")
        todos = {}
        for line in tokenize.generate_tokens(buf.readline):
            if line.type == tokenize.COMMENT:
                todo = self.comment2todo(line.string)
                if todo is None:
                    continue
                todos[line.string] = todo
                
        return todos

    def get_todos_java(self, path: str):
        lines = comment_parser.extract_comments(path, mime=self.MIME_JAVA)
        todos = {}

        for line in lines:
            todo = self.comment2todo(line.string)
            if todo is None:
                continue
            todos[line.string] = todo
        
        return todos

    
    def comment2todo(self, line: string):
        line_idx = line.find(self.TODO_COMMENT)
        
        if line_idx == -1:
            return None

        priority = self.get_priority(line)
        desc = line[line_idx + self.TODO_OFFSET + priority:].strip()
        todo = self.todoist.create_task(self.project_id, description, priority)

        return Todo(todo['id'], desc, priority)
    
    def delete_todos(self, task_ids):
        for task_id in task_ids:
            self.delete_todo(task_id)

    def delete_todo(self, task_id: int):
        self.todoist.delete_task(task_id)
    


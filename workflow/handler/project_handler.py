from sqlitedict import SqliteDict
from ..model.project import Project

class ProjectHandler():
    DATABASE_NAME = './project.sqlite'

    def __init__(self):
        """ Reads projects from database """
        self.projects = self.read_projects()

    @property
    def projects(self):
        """Projects that will be analyzed 
        by the system
        
        Returns:
            dict<str,Project>: projects
        """
        return self._projects

    @projects.setter
    def projects(self, value):
        """Setter for projects property
        
        Args:
            value (dict<str, Project>): new project value
        
        Raises:
            TypeError: property must be a dict
        """
        if isinstance(value, dict):
            raise TypeError("projects must be a dict")

        self._projects = value

    def get_project(self, name: str):
        """Given a project name returns a project object
        from the projects dictionary
        
        Args:
            name (str): name of the project
        
        Returns:
            Project: project object
        """
        return self.projects[name]

    def read_projects(self):
        """Reads projects from a sqlite database
        
        Returns:
            SqliteDict: projects' dictionary
        """
        
        return SqliteDict(self.DATABASE_NAME, autocommit=True)

    def project_exists(self, name):
        """Checks if a project exists in the projects
        dictionary
        
        Args:
            name (str): name of the project
        
        Returns:
            bool: true if exists, false otherwise
        """
        return name in self.projects

    def create_project(self, name: str, id: int, path: str):
        """Creates a project in the dictonary and commits
        changes to the Sqlite database
        
        Args:
            name (str): name of the project
            id (int): id of the project
            path (str): path of the project
        """
        self.projects[name] = Project(id, name, path)
        self.projects.commit()

    def remove_project(self, name: str):
        """Removes project from the projects dict
        
        Args:
            name (str): name of the project
        """
        del self.projects[name]

import uuid, requests, json

class Todoist:
    URL = "https://beta.todoist.com/API/v8"
    PROJECT = "/projects"
    TASK = "/tasks"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def create_project(self, name: str):
        return requests.post(
            self.URL + self.PROJECT,
            data=json.dumps({
                "name": name
            }),
            headers={
                "Content-Type": "application/json",
                "X-Request-Id": str(uuid.uuid4()),
                "Authorization": "Bearer %s" % self.api_key
            }).json()

    def create_task(self, project_id: int, content: str, priority: int):
        return requests.post(
            self.URL + self.TASK,
            data=json.dumps({
                "project_id": project_id,
                "content": content,
                # "due_string": "tomorrow at 12:00",
                # "due_lang": "en",
                "priority": priority
            }),
            headers={
                "Content-Type": "application/json",
                "X-Request-Id": str(uuid.uuid4()),
                "Authorization": "Bearer %s" % self.api_key
            }).json()

    def delete_task(self, task_id):
        return requests.delete(
            self.URL + self.TASK + f"/{task_id}", 
            headers={
                "Authorization": "Bearer %s" % self.api_key
            })

    def get_projects(self):
        return requests.get(
            self.URL + self.PROJECT, 
            headers={
                "Authorization": "Bearer %s" % self.api_key
            }).json()
    
    def project_exists(self, name):
        projects = requests.get(
            self.URL + self.PROJECT, 
            headers={
                "Authorization": "Bearer %s" % self.api_key
            }).json()
        
        for project in projects:
            if project['name'] == name:
                return True
        
        return False


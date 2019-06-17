from github import Github
from todoist import Todoist
from shutil import copy
from project import ProjectManager, Project
from functions import is_internet_up, repo_exists, ask_for_input
from datetime import datetime
import os
import pygit2
import click
import configparser

@click.group()
@click.pass_context
def main(ctx):
    if not is_internet_up():
        print("Please check your intenet connection")
        return
    config = configparser.ConfigParser()
    config.read('config.ini')

    ctx.obj["github"] = Github(config["GITHUB"]["API"])
    ctx.obj["todo_manager"] = TodoManager(config["TODOIST"]["API"])    
    ctx.obj["path"] = config["PATH"]
    ctx.obj["project_manager"] = ProjectManager()

@main.command()
@click.option("--name", help="Name of the project that will be created")
@click.pass_context
def create_project(ctx, name: str):
    
    # if repo_exists(ctx.obj["github"], name):
    #     print("Repo already exists")
    #     return
    
    # if ctx.obj["project_manager"].project_exists(name):
    #     print("Project with the same name already exists in " + ctx.obj["path"])
    #     return
    
    # if ctx.obj["todoist"].project_exists(name):
    #     print("Project with the same name already exists in Todoist")
    #     return

    # # Create Repo
    # repo = ctx.obj["github"].get_user().create_repo(name)
    # repo.create_file("README.md", "Added Readme", "# {}".format(name), branch="master")

    # # Clone and add gitignore
    # repo_path = os.path.join(ctx.obj["path"]["REPO"], name)
    # repo_clone = pygit2.clone_repository(repo.git_url, repo_path)
    # copy(ctx.obj["path"]["GITIGNORE"], repo_path)

    # # Create project in Todoist and project manager
    # todoist_id = ctx.obj["todoist"].create_project(name)['id']
    # ctx.obj["project_manager"].create_project(name, todoist_id, repo_path)
    ctx.obj["project_manager"].create_project(name, 1, "/Users/armando/Documents/test/")

  
@main.command()
@click.option("--name", help="Name of the project that will be created")
@click.pass_context
def check_todos(ctx, name: str):
    if not ctx.obj["project_manager"].project_exists(name):
        print("Project does not exists")
        return

    project = ctx.obj["project_manager"].get_project(name)
    
    old_files = project.files
    curr_files = project.get_current_files()

    old_files_names = set(old_files)
    curr_files_names = set(curr_files)
    
    new_files_names = curr_files_names - old_files_names
    deleted_files_names = old_files_names - curr_files_names

    for deleted_file_name in deleted_files_names:
        deleted_file = old_files[deleted_file_name]

        for todo_name in deleted_file.todos:
            todo = deleted_file.todos[todo_name]
            ctx.obj["todo_manager"].delete_todo(todo.id)
        
        del old_files[deleted_file_name]

    for new_file_name in new_files_names:
        old_files[new_file_name] = curr_files[new_file_name]
        

    for file_name in project.files:
        file = project.get_file(file_name)

        seconds = os.path.getmtime(file.path)
        last_modified = datetime.fromtimestamp(seconds)
        
        if last_modified <= file.last_analyzed:
            continue
        
        file.last_analyzed = last_modified

        

    
def start():
    main(obj={})

if __name__ == "__main__":
    start()
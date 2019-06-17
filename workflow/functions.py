import configparser
from github import Github
from urllib.request import urlopen, URLError

def repo_exists(github: Github, name: str):
    try:
        repo = github.get_user().get_repo(name)
        return True
    except:
        return False

def is_internet_up():
    try:
        urlopen('https://google.com', timeout=1)
        return True
    except URLError as err: 
        return False

def ask_for_input():
    answer = None
    while answer not in ("y", "n"):
        answer = input("Do you want to continue?(y/n)")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please enter y or n.")


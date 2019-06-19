# Workflow

Workflow is a simple cli app to simplify the managment of my projects. I am an avid Todoist user and I like to keep all my
tasks available within the app. This project creates Todoist projects and analyzes source code to import comments with TODO 
tags into Todoist.

### Requirements


### Features 

1. Creates projects
  - Creates a repo in you github account
  - Adds simple README
  - Clones the repo 
  - Moves a basic .gitignore to project
  - Creates a project in Todoist
2. Imports TODO from code to Todoist
  - Extracts comments from source code and imports the todo tags to 

### Config 

```
```

### Usage

```sh
$ preact create <template-name> <project-name>
```

Example:

```sh
$ preact create default my-project
```

### Supported Languages

- Python
- Java 

### CLI Options

#### preact create

Create a project to quick start development.

```sh
$ preact create <template-name> <project-name>

  --name        The application name.
  --cwd         A directory to use instead of $PWD.
  --force       Force option to create the directory for the new app  [boolean] [default: false]
  --yarn        Installs dependencies with yarn.                      [boolean] [default: false]
  --git         Initialize version control using git.                 [boolean] [default: false]
  --install     Installs dependencies.                                [boolean] [default: true]
```

Note: If you don't specify enough data to the `preact create` command, it will prompt the required questions.



### Future Features 

# Workflow

> Start building a [Preact] Progressive Web App in seconds 🔥

### Usage

```sh
$ preact create <template-name> <project-name>
```

Example:

```sh
$ preact create default my-project
```

The above command pulls the template from [preactjs-templates/default], prompts for some information, and generates the project at `./my-project/`.


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

### Requirements


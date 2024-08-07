# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

You can check poetry is installed by running `poetry --version` from a terminal.

**Please note that after installing poetry you may need to restart VSCode and any terminals you are running before poetry will be recognised.**

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

Uncomment the lines:

```markdown
TRELLO_API_KEY=
TRELLO_API_TOKEN=
TRELLO_BOARD_ID=
TRELLO_LIST_ID=
```

And set the environment variables to your corresponding API credentials and board ID.
See instructions [here](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#managing-your-api-key)
and [here](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#boards).

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

The containerised development version of the app (with hot reloading) can be run with the following docker commands:

```bash
$ docker build --target dev --tag todo-app:dev .
$ docker run --rm -it --env-file .env -p 5000:5000 -v ${PWD}/todo_app/:/opt/app/todo_app/ todo-app:dev
```

Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

The production version of the app can be deployed using:

```bash
$ docker build --target prod --tag todo-app:prod .
$ docker run --rm -it --env-file .env -p 5000:5000 todo-app:prod
```

## Deploying the App

Deployment is managed with Ansible.

Create an [inventory file](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html)
with a `webservers` group containing all the hosts to deploy the app to.

Make sure you have SSH access to these hosts.

Then run:
```bash
$ ansible-playbook -i <inventory file> playbook.yaml
```

The app will then be visible at each of the hosts under port `5000`.

## Running Tests

Tests are run using [pytest](https://docs.pytest.org/en/8.0.x/).

To run the tests, run the commands:

```bash
$ docker build --target test --tag todo-app:test .
$ docker run --rm todo-app:test
```

# fastapi-mongodb-template
A Fastapi + Mongodb + beanie template.
This project features a simple but extensible user + role system.

## Quick start guide

### Installation

- [ ] git: https://github.com/git-guides/install-git
- [ ] python >= 3.10: https://www.python.org/downloads/
- [ ] pipenv: pip install --user pipenv

Make sure that pipenv, python and git are available in your PATH

#### Clone the project
```bash
git clone https://github.com/Maydmor/fastapi-mongodb-template.git
```
or when you have an ssh-key setup
```bash
git clone git@github.com:Maydmor/fastapi-mongodb-template.git
```

#### Setup the project

cd into your project folder and install all dependencies by using pipenv

e.g. 
```bash
cd fastapi-mongodb-template
pipenv install
```

when all dependencies are installed, start the virtual environment and run the project using uvicorn.
(NOTE: uvicorn is installed as dependency when you run pipenv install)
```bash
pipenv shell
uvicorn main:app --reload
```

### Project structure

#### models folder
This folder contains all models and schemas. Models that inherit from Document are extended by beanie functionalities,
so that you can simply create, read, update, delete these models in the database

docs: 
https://maydmor.github.io/fastapi-mongodb-template/models

#### repositories folder
This folder contains the repositories which act as an interface for the database.
docs:
https://maydmor.github.io/fastapi-mongodb-template/repositories

#### routers folder
This folder contains all APIRouters. The endpoints for your api should go in here

docs:
https://maydmor.github.io/fastapi-mongodb-template/routers

#### security folder
This folder contains all security related modules and functions. 

docs:
https://maydmor.github.io/fastapi-mongodb-template/security


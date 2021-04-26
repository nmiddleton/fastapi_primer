# Creating the virtual environment

`python -m pip install virtualenv`

`python -m virtualenv .venv`

# Activating virtualenv on Linux Ubuntu /macOS
`source .venv/bin/active`

# Activate virtualenv on Windows 10
`.\.venv\Scripts\activate`

# Upgrade the package manager (e.g. pip)

`python.exe -m pip install --upgrade pip`

# Deactivating the virtual environment
`deactivate`

# Code style helpers and repository ignore
Get the .editorconfig and .gitignore files from https://dev.azure.com/kennedyslaw/Development%20Operations/_git/editorconfig
Add the following line to the bottom of the .gitignore file (so that python packages are not committed to the repo)

`.venv`

# Installing Python dependencies
Ensuring your virtualenv is activated,  and either create a requirement.txt file and install using it.
`pip install -r requirements/requirements.txt`

Or, install the packages manually. finally create a requirements.txt for others to use like this

`pip freeze > requirements.txt`

# Pip install?
If this project is going to be a pip installable, a setup.py will be needed (this is out of scope)

# Project folders
For the most part, only code is kept under the src directory.
When creating subdirectories, if you need some code to be importable, then put an empty file __.init.py__ in the folder with the code. This allows python to recognise the code there as an importable package.
e.g. if you have a python file like..
`./src/services/azurestorage/blobservice.py`

Then add a file to the same dir

`./src/services/azurestorage/__init.py__`

Then this package can be imported into any other python files via

`from services.azurestorage import blobservice`

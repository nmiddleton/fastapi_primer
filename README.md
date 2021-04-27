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

# Structure
Under the source directory are several folders that come together in the "main.py" file. This is a common python convention where, in this case, main.py imports the api, services and the website controller. When main.py is run, the __main__ function sets up configuration and runs the site using uvicorn (a basic webserver).

Note in this set-up that rather than have the api define all the api endpoints, there is a "routing" component that is common to product development design in most. We see here it brings

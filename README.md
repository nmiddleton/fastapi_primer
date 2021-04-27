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
## main.py
Under the source directory are several folders that come together in the `main.py` file. This is a common python convention where, in this case, `main.py` imports the api, services and the website controller. When `python main.py` is run, the `__main__` function calls up configuration and runs the site using uvicorn (a basic webserver).

## Config
The configuration section is present in `main.py` so that settings can be switched in and out if, for example, we want things different from development to production. The configuration "function" could even go into it's own file under"config" to make main.py cleaner.

## Routing the site endpoints
Note in this set-up that there is a "routing" component. This is a pattern that common to development design when moving a prototype to a product. We see here it we can control what is available in the whole site from `main.py`, bringing in routes at this top level from separate sub-components whether they are apis or static files. There is a type of test called acceptance test that can see if the whole system is providing the api endpoints required of it.

## Models
not to be confused with data science models. A model describes a class object from which data structures will be instantiated. In this example a classd of location has properties city,state and country. Tests should be written that will break if these models are changed. This will ensure the models are recognised as a standard shape within the project. These are very simple tests.

## Services
The job of a service is to interface with external things such as databases. In this example it makes a call to an internet site to get a forecast json. As these external systems may change independently of our code, so the service can be amended, leaving everything behind the service oblivious to these changes in implementation. Services should have tests that check the operation against known data. Howwever, since services often communicate with external systems, these tests are often more complicated and involve "faking" the external system and intercepting the calls to it during the test, these are advanced tests and can take some time to develop.

## API
The real purpose of this project is to provide an API that does something on request. See how this API ensures that its parameters are tightly controlled - exepecting the data to match the shape of the Location "model" and abstractly using the "service" to perform an asynchronous task. Also note the use of the @router decoration so that this can be pulled into the main.py routing controller.

By using FastAPI the apis come with ready made documentation (/redoc) and swagger site (/docs) where a user can test the API using a browser.

Testing of API behaviour is also quite simple unit testing to set up.

## Web
The web folder is only for front-end components, there may not be a web folder if this is just an API project. The swagger site may be enough for a user to work out the API usage. A simple web page is just given for example.


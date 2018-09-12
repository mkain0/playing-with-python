# flask-rest-api

First Python REST API using:

 * python 3.5
 * virtualenv
 * flask
 * SQLite
 
# Local Deployment

Open the folder **flask-rest-api** with your text editor or IDE. 
Create a virtual environment and install the dependencies:

`pip install -r production.txt`

Active your virtual environment and set the **FLASK_APP=main.py** in your terminal session, and then execute:

`flask run`

You should have access through: 

`http://localhost:5000/music-archive/api/v1`

As example to run a test:

`py.test test/integration/test_artists.py`

# Testing Environment

If you want to test the API:

`https://playing-with-python.herokuapp.com/music-archive/api/v1/`

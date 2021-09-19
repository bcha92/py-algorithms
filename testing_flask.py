# Test running python with Flask module from PIP

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World"

app.run(port=8000)
# In certain situations, the port number may need
# to be in quotes ('8000') or without (8000)

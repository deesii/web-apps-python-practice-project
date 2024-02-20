import os
from flask import Flask, request

app = Flask(__name__)

# Let's look at an example where Flask receives this request:
# > GET /

# There are a number of routes. We'll look through each one in turn and see if
# it matches.

@app.route('/', methods=['POST'])
def post_index():
    # DOES NOT RUN: The HTTP method (GET) doesn't match the route's (POST)
    return "Not me! :("

@app.route('/hello', methods=['GET'])
def get_hello():
    # DOES NOT RUN: The path (`/hello`) doesn't match the route's (`/`)
    return "Not me either!"

@app.route('/', methods=['GET'])
def get_index():
    # RUNS: This route matches! The code inside the block will be executed now.
    return "I am the chosen one!"

@app.route('/', methods=['GET'])
def other_get_index():
    # DOES NOT RUN: This route also matches, but will not be executed.
    # Only the first matching route (above) will run.
    return "It isn't me, the other route stole the show"

# must import `request` too

# Request:
# GET /hello?name=David

@app.route('/hello_name', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"

# POST parameter.. 

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

# To make a request, run:
# curl "http://localhost:5000/hello?name=David"
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

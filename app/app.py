import datetime
import json

from flask import Flask

app = Flask("g611")


@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to our web app!</h1>"


@app.route("/api/v1/version", methods=["GET"])
def version():
    response = {
        "name": "G611",
        "version": "v0.0.1",
        "last_call": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    }
    response = json.dumps(response)
    return response, 200


app.run(port=5611, debug=True)
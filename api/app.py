import datetime
import json

from flask import Flask, request

from api.account import signup
from api.repository import CONNECTION_STRING

app = Flask("g611")


@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to our web api!</h1>"


@app.route("/api/v1/version", methods=["GET"])
def version():
    response = {
        "name": "G611",
        "version": "v0.0.1",
        "last_call": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    }
    response = json.dumps(response)
    return response, 200


@app.route("/api/v1/register", methods=["POST"])
def register():
    try:
        body = request.json
        signup(body, CONNECTION_STRING)
        return "", 204
    except ValueError as ve:
        error_message = {
            "error": f"Invalid request parameters."
        }
        response = json.dumps(error_message)
        return response, 400
    except Exception as e:
        error_message = {
            "error": f"Something went wrong. Cause {e}."
        }
        response = json.dumps(error_message)
        return response, 500


app.run(port=5611, debug=True)
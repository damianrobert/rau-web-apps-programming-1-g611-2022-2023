import datetime
import json

from flask import Flask, request

from api.account import signup, get_user_details, delete_user
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


@app.route("/api/v1/accounts/<user_id>", methods=["GET", "PUT", "DELETE"])
def accounts(user_id):
    if request.method == "GET":
        try:
            user = get_user_details(user_id, CONNECTION_STRING)
            response = user.to_json()
            return response, 200
        except Exception as e:
            error_message = {
                "error": f"Failed to get user details. Cause {e}."
            }
            response = json.dumps(error_message)
            return response, 500

    if request.method == "PUT":
        pass

    if request.method == "DELETE":
        try:
            delete_user(user_id, CONNECTION_STRING)
            return "", 204
        except Exception as e:
            error_message = {
                "error": f"Failed to delete user. Cause {e}."
            }
            response = json.dumps(error_message)
            return response, 500


app.run(port=5611, debug=True)
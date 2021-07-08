# Example code, write your program here
import ipaddress
import json
import re

import pandas as pd
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

EMAIL_REGEX = r'(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'

@app.route("/query")
def query():
    email = request.args.get("email")
    if not re.match(EMAIL_REGEX, email):
        return Response(status=400)
    ip = request.args.get("ip")
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return Response(status=400)
    df = pd.read_csv("data.csv")
    result = df[(df["email"] == email) & (df["ip_address"] == ip)]
    if result.empty:
        return Response(status=404)
    dict_ = result.loc[result.index[0],:].to_dict()
    output_dict = {
        "first_name": dict_["first_name"],
        "last_name": dict_["last_name"],
        "gender": dict_["gender"],
    }
    return jsonify(output_dict)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)
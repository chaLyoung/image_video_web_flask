# -*- coding: UTF-8 -*-
import sys
import os
from flask import Flask, request, jsonify
import flask

app = Flask(__name__)


@app.route('/', methods=['POST', "GET"])
def app_start():
    print("success")
    path = "C:"
    file_list = os.listdir(path)
    return str(file_list)


if __name__ == '__main__':
    app.run(debug=True, port=5003)
"""Globex billing service: tiny Flask app used in the LoopIQ release demo."""
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = "1.3.2"


@app.get("/health")
def health():
    return jsonify(status="ok", version=VERSION)

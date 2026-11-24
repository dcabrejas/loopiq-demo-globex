"""Globex billing service: tiny Flask app used in the LoopIQ release demo."""
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = "1.4.0"


@app.get("/health")
def health():
    return jsonify(status="ok", version=VERSION)


@app.get("/invoices/<invoice_id>")
def invoice(invoice_id):
    return jsonify(id=invoice_id, status="paid")

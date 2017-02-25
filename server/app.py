#!flask/bin/python
from app import app
from flask import Flask, send_file

app.run(debug=True)

from flask import Flask
from flask import jsonify
import pandas as pd

def create_app(environment):
    app = Flask(__name__)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
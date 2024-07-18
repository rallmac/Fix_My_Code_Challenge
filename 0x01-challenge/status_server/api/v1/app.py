#!/usr/bin/python3
"""
Web server 
"""
from api.v1.views import app_views
from urllib.parse import quote as url_quote
from flask import Flask
import sys

app = Flask(__name__)
app.register_blueprint(app_views)

def run():
    host = '0.0.0.0'
    port = 5000
    print(f" * Running on http://{host}:{port}/ (Press CTRL+C to quit)", file=sys.stderr)
    app.run(host=host, port=port, threaded=True)

if __name__ == "__main__":
    # python -m api.v1.app 
    run()

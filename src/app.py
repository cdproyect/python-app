"""Flask Application Module.

This module initializes and runs the Flask Web application.

"""

# 1. Standard library imports FIRST
from datetime import datetime
import socket

# 2. Third-party imports SECOND
from flask import Flask, jsonify  # type: ignore[reportMissingImports]

app = Flask(__name__)
@app.route('/api/v1/info')

def info():
    """Return message info using json format."""
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'Hello Pika Pika! :) Now, there is CD real support yeah!!',
        'deployed_on': 'kubernetes'
    })

@app.route('/api/v1/healthz')

def healthz():
    """Return health status of the application."""
    # Do an actual check here
    return jsonify({
        'status': 'up'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

from flask import Flask, jsonify  # type: ignore[reportMissingImports]
import datetime
import socket

app = Flask(__name__)
@app.route('/api/v1/info')

def info():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'Hello Pika Pika! :) Now, there is CD real support yeah!!',
        'deployed_on': 'kubernetes'
    })

@app.route('/api/v1/healthz')

def healthz():
    # Do an actual check here
    return jsonify({
        'status': 'up'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


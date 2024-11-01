from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
socketio = SocketIO(app)

clients = []

@app.route('/')
def index():
    return render_template('index.html')  # This will point to your HTML file

@socketio.on('connect')
def handle_connect():
    clients.append(request.sid)  # Keep track of connected clients
    emit('message', {'data': 'Client connected!'}, broadcast=True)

@socketio.on('message')
def handle_message(data):
    emit('message', {'data': data['data']}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    clients.remove(request.sid)
    emit('message', {'data': 'Client disconnected!'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)

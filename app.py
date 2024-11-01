from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
socketio = SocketIO(app)

clients = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    clients.append(request.sid)  # Keep track of connected clients
    emit('message', {'data': 'A new client has joined!'}, broadcast=True)

@socketio.on('message')
def handle_message(data):
    emit('message', {'data': data['data']}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    clients.remove(request.sid)
    emit('message', {'data': 'A client has disconnected!'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# In-memory storage for messages
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@socketio.on('message')
def handle_message(msg):
    messages.append(msg)  # Store the message
    send(msg, broadcast=True)  # Broadcast the message to all clients

if __name__ == '__main__':
    socketio.run(app)

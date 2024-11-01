# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Socket event for toggling lights
@socketio.on('toggle_light')
def handle_toggle_light(data):
    # Broadcast the light state to all clients
    emit('light_state', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)

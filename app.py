from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('toggle_event')
def handle_toggle_event(data):
    # Backend processing logic
    response = data.get('action', 'default')
    socketio.emit('response_event', {'result': response})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)

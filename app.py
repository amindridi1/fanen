from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"
socketio = SocketIO(app)

users = []

@app.route("/")
def index():
    if "username" in session:
        return render_template("chatroom.html", username=session["username"])
    else:
        return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    session["username"] = username
    users.append(username)
    return render_template("chatroom.html", username=username)

@app.route("/logout")
def logout():
    session.pop("username", None)
    users.remove(session["username"])
    return render_template("index.html")

@socketio.on("send_message")
def handle_send_message(data):
    emit("receive_message", {"username": session["username"], "message": data["message"]}, broadcast=True)

@socketio.on("connect")
def handle_connect():
    emit("user_joined", {"username": session["username"]}, broadcast=True)

@socketio.on("disconnect")
def handle_disconnect():
    emit("user_left", {"username": session["username"]}, broadcast=True)
    users.remove(session["username"])

if __name__ == "__main__":
    socketio.run(app, debug=True)

from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
# i'm doubting that the session might bring problem, because its likely not compatible with this file's code styilng

from werkzeug.exceptions import abort

from app.routes.auth import login_required
from app.db import get_db

from flask_socketio import (SocketIO, join_room, leave_room, send)
from string import ascii_uppercase
import random



bp = Blueprint('peerchat', __name__)
socketio = SocketIO()



rooms = {}
def generate_unique_code(Length):
    while True:
        code = ""
        for _ in range(Length):
            code += random.choice(ascii_uppercase)


        if code not in rooms:
            break

    return code


# bp = Blueprint('peerchat', __name__)

@bp.route("/help/peer-forum", methods=["POST", "GET"])
def peer_forum():
    session.clear()
    if request.method == 'POST':
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        if not name:
            return render_template("help/peer-forum.html", error = "Please enter a name", code = code, name = name)
        
        if join != False and not code:
            return render_template("help/peer-forum.html", error = "Please enter a code", code = code, name = name)
        
        room = code
        if create != False:
           room = generate_unique_code(4)
           rooms[room] = {"members": 0, "messages": []}

        elif code not in rooms:
            return render_template("help/peer-forum.html", error = "Room does not exist", code = code, name = name)
        
        session["room"] = room
        session["name"] = name

        return redirect(url_for("peerchat.room"))  ##############################url


    return render_template("help/peer-forum.html")


@bp.route("/help/room", methods = ["POST", "GET"])
def room():
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
        return redirect(url_for("peerchat.peer_forum"))
    

    return render_template("help/room.html", code=room, messages=rooms[room]["messages"])



@socketio.on("connect")
def connect():
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    
    if room not in rooms:
        leave_room(room)
        return
    
    join_room(room)
    send({"name": name, "message": "joined room " + room}, to=room)  # Notify room members about the new user
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")

    # # Update the messages list to include the join message
    # rooms[room]["messages"].append({"name": name, "message": f"joined room {room}"})
    

@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]

    send({"name": name, "message": "has left the room"}, to=room)  # Notify room members about the user leaving
    print(f"{name} has left the room {room}")

    # # Update the messages list to include the leave message
    # rooms[room]["messages"].append({"name": name, "message": "has left the room"})


@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return
    
    name = session.get("name")
    if name is None:
        return
    
    message_content = data.get("message")
    if message_content is None:
        return
    
    # Insert message into database
    insert_message(name, message_content)
    
    # Broadcast message to room members
    content = {
        "name": session.get("name"),
        "message": message_content
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {message_content}")

def insert_message(name, message_content):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message_content))
        db.commit()
    except Exception as e:
        print(f"Error inserting message into database: {e}")
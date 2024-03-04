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


app = None
socketio = SocketIO(app)


rooms = {}
def generate_unique_code(Length):
    while True:
        code = ""
        for _ in range(Length):
            code += random.choice(ascii_uppercase)


        if code not in rooms:
            break

    return code


bp = Blueprint('peerchat', __name__)

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


# Function to insert a message into the messages table
def insert_message(name, message):
    db = get_db()
    db.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message))
    db.commit()

    # try:
    #     cursor = conn.cursor()
    #     cursor.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message))
    #     conn.commit()
    # except sqlite3.Error as e:
    #     print(e)


@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    
    if room not in rooms:
        leave_room(room)
        return
    
    join_room(room)
    send({"name": name, "message": "has entered the room"}, to=room)
    rooms[room]["members"] +=1
    print(f"{name} joined room {room}")


    
    insert_message(name, "has entered the room")
    print(f"{name} joined room {room}")



@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -=1
        if rooms[room]["members"] <= 0:
            del rooms[room]

    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")


    insert_message(name, "has left the room")

    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -=1
        if rooms[room]["members"] <= 0:
            del rooms[room]

    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")
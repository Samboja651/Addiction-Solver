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
from app.__init__ import create_app 


socketio = SocketIO(create_app())


rooms = {}
def generate_unique_code(Length):
    while True:
        code = ""
        for _ in range(Length):
            code += random.choice(ascii_uppercase)


        if code not in rooms:
            break

    return code


bp = Blueprint('peer-chat', __name__)

@bp.route("/peer-forum", methods=["POST", "GET"])
def peer_forum():
    session.clear()
    if request.method == 'POST':
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        if not name:
            return render_template("peer-forum.html", error = "Please enter a name", code = code, name = name)
        
        if join != False and not code:
            return render_template("peer-forum.html", error = "Please enter a code", code = code, name = name)
        
        room = code
        if create !=False:
           room = generate_unique_code(4)
           rooms[room] = {"members": 0, "messages": []}

        elif code not in rooms:
            return render_template("peer-forum.html", error = "Room does not exist", code = code, name = name)
        
        session["room"] = room
        session["name"] = name

        return redirect(url_for("room"))


    return render_template("peer-forum.html")

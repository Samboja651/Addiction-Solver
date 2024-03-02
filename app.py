from flask import Flask, render_template, request, redirect, url_for, session, flash, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import sqlite3
from flask_socketio import SocketIO, join_room, leave_room, send
import random
from flask_socketio import join_room, leave_room, send, SocketIO
from string import ascii_uppercase



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.secret_key = 'secret_key'

db = SQLAlchemy(app)
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
   

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.username}>'

def get_db():
    db = sqlite3.connect('app.db')
    return db

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT user_name, story, story_url FROM success_stories')
        stories = cursor.fetchall()

    return render_template('home.html', stories=stories)
        # return "Form submitted successfully!"



# create an account
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('register'))

        # Password conditions
        if len(password) < 8:
            flash('Password must be at least 8 characters long.', 'danger')
            return redirect(url_for('register'))
        elif not any(char.isupper() for char in password):
            flash('Password must contain at least one uppercase letter.', 'danger')
            return redirect(url_for('register'))
        elif not any(char.islower() for char in password):
            flash('Password must contain at least one lowercase letter.', 'danger')
            return redirect(url_for('register'))
        elif not any(char.isdigit() for char in password):
            flash('Password must contain at least one numeric digit.', 'danger')
            return redirect(url_for('register'))
        elif not any(char.isalnum() or char in '!@#$%^&*()-_=+[]{}|;:\'",.<>?/`~' for char in password):
            flash('Password must contain at least one special character.', 'danger')
            return redirect(url_for('register'))

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
            session['username'] = username
            return redirect(url_for('home', username=username))

        else:
            error_message = "Invalid credentials. Please try again."
            return render_template('login.html', error=error_message)  

    return render_template('login.html')


# Delete a user
@app.route('/delete_account/<username>', methods=['GET', 'POST'])
def delete_user(username):
    if request.method == 'POST':
        try:
            user = User.query.get(username)

            if user:
                db.session.delete(user)
                db.session.commit()

                # If the user is logged in, remove the username from the session
                if 'username' in session:
                    session.pop('username', None)

                return redirect(url_for('first_page'))
            else:
                # User not found, redirect to an error page or handle appropriately
                return redirect(url_for('error_page'))
        except Exception as e:
            # Log the exception or handle it as appropriate for your application
            print(f"Error deleting user: {e}")
            db.session.rollback()  # Rollback changes to the database
            abort(500)  # Internal Server Error

    return render_template('delete_account_confirmation.html', username=username)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # Remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('home'))



# redirect to the full story based on user id
@app.route('/<id>', methods=['GET', 'POST'])
def my_story(id):
    base_url = 'http://localhost:8000/'
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT user_id FROM success_stories')
    storyid = cursor.fetchall()

    for ids in storyid:
        if str(ids[0]) == id:
            base_url += str(id[0])
            return render_template('my_story.html')
    



#  # Placeholder for storing chat messages
peer_to_peer_chat = []
doctor_chat = []


# Endpoint for receiving and sending peer-to-peer chat messages
# @app.route('/peer-chat', methods=['POST'])
# def peer_chat():
#     message = request.form.get('message')
#     peer_to_peer_chat.append(message)
#     return jsonify({'messages': peer_to_peer_chat})

# # Endpoint for receiving and sending doctor chat messages
# @app.route('/doctor-chat', methods=['POST'])
# def doctor_chat():
#     message = request.form.get('message')
#     doctor_chat.append(message)
#     return jsonify({'messages': doctor_chat})





@app.route("/peer-forum", methods=["POST", "GET"]) 
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


@app.route("/room", methods = ["POST", "GET"])
def room():
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
        return redirect(url_for("peer-forum"))
    

    return render_template("room.html", code=room, messages=rooms[room]["messages"])

@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return
    
    name = session.get("name")
    if name is None:
        return
    
    # Get message content
    message_content = data.get("data")
    if message_content is None:
        return

    # Insert message into the database
    conn = create_connection()
    if conn is not None:
        insert_message(conn, name, message_content)
        conn.close()
    
    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")



def create_connection():
    try:
        conn = sqlite3.connect("app.db")
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

# Function to create the messages table if it doesn't exist
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            message TEXT NOT NULL,
                            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )''')
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Function to insert a message into the messages table
def insert_message(conn, name, message):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Connect to the SQLite database
conn = create_connection()
if conn is not None:
    # Create messages table if not exists
    create_table(conn)
    conn.close()
else:
    print("Error! Cannot create the database connection.")

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


    conn = create_connection()
    if conn is not None:
        insert_message(conn, name, "has entered the room")
        conn.close()
        # print(f"{name} joined room {room}")

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

    conn = create_connection()
    if conn is not None:
        insert_message(conn, name, "has left the room")
        conn.close()




@app.route('/help', methods=['GET'])
# -----------code inherits operation from previous help page -------------
@app.route('/help', methods=['GET', 'POST'])
def help():
    if request.method == 'GET':
        return render_template('help_platform.html')
    
    
    if request.method == 'POST':
        required_fields = ['addiction-type', 'duration', 'cause', 'severity', 'age', 'gender']
        form_data = {field: request.form.get(field) for field in required_fields}
        data = list(form_data.values())

        if not all(form_data.values()):
            return "Please fill in all fields." 

        conn = get_db()
        cursor = conn.cursor()

        # get the logged in user's id
        stmid = 'SELECT user_id FROM user ORDER BY user_id DESC'
        # .fetchone returns a tuple like (3,) so to get the int itself i use indexing
        user_id = cursor.execute(stmid).fetchone()[0]
        # now add the user_id to the list of data to be inserted into db
        data.append(user_id)

        stm = 'INSERT INTO addiction_data (addiction_type, duration, cause, severity, age, gender, user_id) VALUES(?, ?, ?, ?, ?, ?, ?)'
        cursor.execute(stm, data)

        # print(data)
        conn.commit()
        conn.close()

        return render_template('help_platform.html') 
    


@app.route('/educational_resources', methods=['GET', 'POST'])
def educational_resources():
    books = [
        {"title": "The Biology of Desire: Why Addiction Is Not a Disease", "author": "Marc Lewis"},
        {"title": "Addiction: A Disorder of Choice", "author": "Gene M. Heyman"},
        {"title": "Clean: Overcoming Addiction and Ending America’s Greatest Tragedy", "author": "David Sheff"}
    ]

    videos = [
        {"title": "TED Talk: Everything You Think You Know About Addiction is Wrong", "speaker": "Johann Hari", "link": "https://www.youtube.com/watch?v=PY9DcIMGxMs"},
        {"title": "The Opposite of Addiction is Connection", "speaker": "Johann Hari", "link": "https://www.youtube.com/watch?v=PY9DcIMGxMs"},
        {"title": "Pleasure Unwoven: An Explanation of the Brain Disease of Addiction", "speaker": "Kevin McCauley", "link": "https://www.youtube.com/watch?v=ao8L-0nSYzg"}
    ]

    return render_template('educational_resources.html', books=books, videos=videos)
          

# Endpoint for receiving and sending peer-to-peer chat messages
# @app.route('/peer-forum', methods=['GET', 'POST'])
# def peer_forum():
#     if request.method == 'GET':
#         return render_template('peer-forum.html')
    


@app.route('/chat-doctor', methods=['GET'])
def chat_doctor():
    if request.method == 'GET':
        return render_template('chat-doctor.html')

# def connect_db():
#     return sqlite3.connect('app.db')


# # Function to add a new message to the messages table
# def add_message(content):
#     # try:
#         conn = connect_db()
#         cursor = conn.cursor()
#         cursor.execute('INSERT INTO messages (content) VALUES (?)', (content,))
#         conn.commit()
#         conn.close()
#     #     print("Message added successfully.")
#     # except sqlite3.Error as e:
#     #     print("Error adding message:", e)

# # Function to delete a message from the messages table
# def delete_message(message_id):
#     # try:
#         conn = connect_db()
#         cursor = conn.cursor()
#         cursor.execute('DELETE FROM messages WHERE id = ?', (message_id,))
#         conn.commit()
#         conn.close()
#     #     print("Message deleted successfully.")
#     # except sqlite3.Error as e:
#     #     print("Error deleting message:", e)

# # Function to retrieve all messages from the messages table
# def get_messages():
#     try:
#         conn = connect_db()
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM messages')
#         messages = cursor.fetchall()
#         conn.close()
#         return messages
#     except sqlite3.Error as e:
#         print("Error retrieving messages:", e)
#         return []


if __name__ == '__main__':
    app.run(debug=True, port=3000)

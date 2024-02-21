from flask import Flask, render_template, request, redirect, url_for, session, flash, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import sqlite3


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_credentials.db'
app.secret_key = 'secret_key'

db = SQLAlchemy(app)

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
@app.route('/<user_id>/mystory/<name>', methods=['GET', 'POST'])
def my_story(user_id, name):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT user_id, user_name FROM success_stories')
    ids = cursor.fetchall()

    if request.method == 'GET':
        if int (user_id) == ids[0][0]:
            return render_template('my_story.html', username = ids[0][1])
        elif int (user_id) == ids[1][0]:
            return render_template('my_story.html', username = ids[1][1])
        elif int (user_id) == ids[2][0]:
            return render_template('my_story.html', username = ids[2][1])
        elif int (user_id) == ids[3][0]:
            return render_template('my_story.html', username = ids[3][1])
        elif int (user_id) == ids[4][0]:
            return render_template('my_story.html', username = ids[4][1])
        elif int (user_id) == ids[5][0]:
            return render_template('my_story.html', username = ids[5][1])
        elif int (user_id) == ids[6][0]:
            return render_template('my_story.html', username = ids[6][1])
        elif int (user_id) == ids[7][0]:
            return render_template('my_story.html', username = ids[7][1])
        elif int (user_id) == ids[8][0]:
            return render_template('my_story.html', username = ids[8][1])
        elif int (user_id) == ids[9][0]:
            return render_template('my_story.html', username = ids[9][1])
        elif int (user_id) == ids[10][0]:
            return render_template('my_story.html', username = ids[10][1])
        else:
            return redirect('/')




 # Placeholder for storing chat messages
peer_to_peer_chat = []
doctor_chat = []


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
          

# Endpoint for receiving and sending peer-to-peer chat messages
@app.route('/peer-forum', methods=['GET'])
def peer_forum():
    if request.method == 'GET':
        return render_template('peer-forum.html')

@app.route('/chat-doctor', methods=['GET'])
def chat_doctor():
    if request.method == 'GET':
        return render_template('chat-doctor.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

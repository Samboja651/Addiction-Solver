from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    db = sqlite3.connect('app.db')
    return db

@app.route('/', methods=['GET', 'POST'])
def test_stories():
    if request.method == 'GET':
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT user_name, story FROM success_stories')
        stories = cursor.fetchall()

        return render_template('f_stories.html', stories=stories)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        required_fields = ['addiction-type', 'duration', 'cause', 'severity', 'age', 'gender']
        form_data = {field: request.form.get(field) for field in required_fields}

        if not all(form_data.values()):
            return "Please fill in all fields."

        return "Form submitted successfully!"

    return render_template('f_stories.html')

app = Flask(__name__)

# Placeholder for storing chat messages
peer_to_peer_chat = []
doctor_chat = []

@app.route('/')
def help_page():
    return render_template('help.html')

# Endpoint for receiving and sending peer-to-peer chat messages
@app.route('/peer-chat', methods=['POST'])
def peer_chat():
    message = request.form.get('message')
    peer_to_peer_chat.append(message)
    return jsonify({'messages': peer_to_peer_chat})

# Endpoint for receiving and sending doctor chat messages
@app.route('/doctor-chat', methods=['POST'])
def doctor_chat():
    message = request.form.get('message')
    doctor_chat.append(message)
    return jsonify({'messages': doctor_chat})

if __name__ == '__main__':
    app.run(debug=True,port=8000)
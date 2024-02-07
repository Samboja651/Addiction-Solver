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

@app.route('/educational_resources')
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

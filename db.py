import sqlite3
from app import db

def init_db():
    db = sqlite3.connect('app.db')
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS form_data (
            user_id INTEGER PRIMARY KEY,
            user_name TEXT NOT NULL,
            type_of_addiction VARCHAR(255) NOT NULL,
            duration INTEGER NOT NULL,
            possible_cause VARCHAR(255),
            severity INTEGER NOT NULL,
            age INTEGER NOT NULL,
            gender VARCHAR(10) NOT NULL,
            phone_number VARCHAR(12) NOT NULL,
            email VARCHAR(255) NOT NULL,
            submission_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS peer_forum_data (
            message_id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            message_content TEXT NOT NULL,
            phone_number VARCHAR(12) NOT NULL,
            email VARCHAR(255) NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES form_data(user_id),
            FOREIGN KEY (phone_number) REFERENCES form_data(phone_number),
            FOREIGN KEY (email) REFERENCES form_data(email)
        )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS doctors (
            doctor_id INTEGER PRIMARY KEY,
            doctor_name TEXT NOT NULL,
            phone_number VARCHAR(12),
            email VARCHAR(255),
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS personalized_chats (
            chat_id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            doctor_id INTEGER NOT NULL,
            message_content TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES form_data(user_id),
            FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) 
        )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS educational_resources (
            resource_id INTEGER PRIMARY KEY,
            resource_type VARCHAR(50) NOT NULL,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            link VARCHAR(255) NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS success_stories (
                   story_id INTEGER PRIMARY KEY,
                   user_id INTEGER,
                   user_name TEXT NOT NULL,
                   story TEXT NOT NULL,
                   story_url TEXT NOT NULL,
                   timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   FOREIGN KEY (user_id) REFERENCES form_data(user_id)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY,
                   username VARCHAR(80) UNIQUE NOT NULL,
                   password VARCHAR(120) UNIQUE NOT NULL
    )""")

    # Create the messages table
    cursor.execute("""CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            user TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")

    db.commit()

init_db()




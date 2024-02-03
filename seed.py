import sqlite3

DATABASE = 'app.db'

def seed_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    success_stories = [
        ("1", "Jane Wawuda", "I can now live a more productive life because with the help of this system I broke the chains of Alcoholism. I guarantee and recommend that you will have a progressive journey.", "http://localhost:5000/1"),
        ("2", "Abdallah Masoud", "After struggling with addiction for years, I decided to seek help. Through counseling and support from this addiction solver app, I successfully overcame my addiction. Today, I am living a healthier and happier life.", "http://localhost:5000/2"),
        ("3", "John Majiba", "My journey with this application has helped me to practice self control against browsing unproductively on social media.", "https://developer.mozilla.org/en-US/docs/Web/API/Element/getAttribute")
    ]

    # form_data = [
    #     ("Jane Wawuda", "Alcoholism", "5", "inheritance from parents", "6", "32", "Female", "+254724987423", "jane@gmail.com"),
    #     ("Abdallah Masoud", "Smoking", "6", "Peer influence", "3", "35", "Male", "+23589562314", "masoud@gmail.com"),
    #     ("John Majiba", "Social Media", "7", "Bad habit", "9", "43", "Male", "+26589347820", "majiba@gmail.com")
    # ]

    cursor.executemany('INSERT INTO success_stories (user_id, user_name, story, story_url) VALUES (?, ?, ?, ?)', success_stories)
    # cursor.executemany('INSERT INTO form_data (user_name, type_of_addiction, duration, possible_cause, severity, age, gender, phone_number, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', form_data)

    conn.commit()
    conn.close()

seed_db()
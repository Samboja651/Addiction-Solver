import sqlite3

DATABASE = 'app.db'

def seed_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    success_stories = [
        ("Jane Wawuda", "I can now live a more productive life because with the help of this system I broke the chains of Alcoholism. I guarantee and recommend that you will have a progressive journey."),
        ("Abdallah Masoud", "After struggling with addiction for years, I decided to seek help. Through counseling and support from this addiction solver app, I successfully overcame my addiction. Today, I am living a healthier and happier life."),
        ("John Majiba", "My journey with this application has helped me to practice self control against browsing unproductively on social media.")
    ]

    cursor.executemany('INSERT INTO success_stories (user_name, story) VALUES (?, ?)', success_stories)
    conn.commit()
    conn.close()

seed_db()
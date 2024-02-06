import sqlite3

DATABASE = 'app.db'

def seed_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    success_stories = [
        ("1", "Jane Wawuda", "I can now live a more productive life because with the help of this system I broke the chains of Alcoholism. I guarantee and recommend that you will have a progressive journey.", "http://localhost:8000/1"),
        ("2", "Abdallah Masoud", "After struggling with addiction for years, I decided to seek help. Through counseling and support from this addiction solver app, I successfully overcame my addiction. Today, I am living a healthier and happier life.", "http://localhost:8000/2"),
        ("3", "John Majiba", "My journey with this application has helped me to practice self control against browsing unproductively on social media.", "http://localhost:8000/3"),
        ("4", "Isaack Kulot", "I've tried so many times, but The Addiction Solver helped me make it work. After 10 years in addiction, my kids finally call me 'Daddy' again.", "http://localhost:8000/4"),
        ("5", "Joanna Macabus", "Through the trusting guidance of the programs of Addiction Solver, I finally had the courage to go back and make peace with the demons inside me.", "http://localhost:8000/5"),
        ("6", "Mirriam Nimo", "It felt like I search a million treatment centers, The Addiction Solver was the only one that helped me about what was happening to our daughter…and our family.", "http://localhost:8000/6"),
        ("7", "William Namanu", "The Addiction Solver was the complete opposite of what I expected or had gone through in other programs. I found myself looking forward to sessions and feeling the weight lifting off of my shoulders with every new day.", "http://localhost:8000/7"),
        ("8", "William", "This is where I learned to deal with my problems properly instead of running away. I learned that I mattered.", "http://localhost:8000/8"),
        ("9", "Kelvin Ogembo", "I'm 9 years sober thanks to Addiction Solver helping me reconnect to myself & God.", "http://localhost:8000/9"),
        ("10", "Christine Ngandi", "In just 30 days, my doctor at Addiction Solver helped me find a special person I didn't realize lived inside of me.", "http://localhost:8000/10")
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
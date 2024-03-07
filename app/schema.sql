-- users table
CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(80) UNIQUE NOT NULL,
    password VARCHAR(120) UNIQUE NOT NULL
);

-- user's addiction info
CREATE TABLE IF NOT EXISTS addiction_data (
    addiction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    addiction_type VARCHAR(255) NOT NULL,
    duration INTEGER NOT NULL,
    cause VARCHAR(255),
    severity INTEGER NOT NULL,
    age INTEGER NOT NULL,
    gender VARCHAR(10) NOT NULL,
    user_id INTEGER UNIQUE NOT NULL,
    submission_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

-- message in user forum
CREATE TABLE IF NOT EXISTS peer_forum_chat (
    message_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    message_content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

-- record for doctors
CREATE TABLE IF NOT EXISTS doctors (
    doctor_id INTEGER PRIMARY KEY,
    doctor_name VARCHAR(50) NOT NULL,
    proffession VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- user conversation with doctor
CREATE TABLE IF NOT EXISTS user_doctor_chat (
    chat_id INTEGER PRIMARY KEY,
    user_id INTEGER UNIQUE,
    doctor_id INTEGER UNIQUE,
    message_content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) 
);

-- educational resources
CREATE TABLE IF NOT EXISTS educational_resources (
    resource_id INTEGER PRIMARY KEY,
    resource_type VARCHAR(50) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    link VARCHAR(255) NOT NULL
);

--addiction types
CREATE TABLE IF NOT EXISTS addiction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    addiction_type TEXT,
    resource_id INTEGER UNIQUE,
    FOREIGN KEY(resource_id) REFERENCES educational_resources(resource_id)
);

--severity types
CREATE TABLE IF NOT EXISTS severity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    severity_type TEXT,
    resource_id INTEGER UNIQUE,
    FOREIGN KEY(resource_id) REFERENCES educational_resources(resource_id)
);


CREATE TABLE IF NOT EXISTS success_stories (
    story_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    user_name TEXT NOT NULL, -- to remove username, can be accessed using user_id
    story VARCHAR(250) NOT NULL,
    story_url VARCHAR(100) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES form_data(user_id)
);

CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    message TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
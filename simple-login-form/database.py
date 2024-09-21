import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)""")

cursor.execute("""
INSERT INTO users (username, password, name, email) VALUES
('user1', 'pass123', 'Kallu Don', 'kalluishere@gmail.com'),
('user2', 'pass456', 'Billa Don', 'billakumar@gmail.com'),
('user3', 'pass789', 'Kallu Kasai', 'kaisahaimerabhai@gmail.com')
""")

conn.commit()
conn.close()
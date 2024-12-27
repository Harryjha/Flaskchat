import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the 'responses' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL
    )
''')

# Insert predefined responses into the table
responses = [
    ('hello', 'Hi! How can I assist you?'),
    ('how are you', 'I\'m doing great, thanks for asking!'),
    ('bye', 'Goodbye! Have a great day!')
]

cursor.executemany('''
    INSERT INTO responses (question, answer)
    VALUES (?, ?)
''', responses)

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("Database setup complete with predefined responses!")


from flask import Flask, jsonify, request, send_from_directory
import sqlite3
from flask_cors import CORS  # Importing CORS

app = Flask(__name__)


CORS(app)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('database.db')  # SQLite or your preferred DB
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return send_from_directory('static', 'chatbot-ui.html') 

# Route: API to fetch chatbot responses
@app.route('/predict', methods=['POST'])
def predict():
    user_message = request.json.get('message', '').lower()
    print(f"User Message: {user_message}")  # Debug log for user input

    # Query the database for a response
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    response = cursor.execute("SELECT answer FROM responses WHERE question = ?", (user_message,)).fetchone()
    conn.close()

    # Check if a response was found
    if response:
        print(f"Bot Response: {response[0]}")  # Debug log for bot response
        return jsonify({'answer': response[0]})
    else:
        print("Bot Response: Sorry, I don't understand that question.")  # Debug log for no response
        return jsonify({'answer': 'Sorry, I don\'t understand that question. Please try again.'})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5001)

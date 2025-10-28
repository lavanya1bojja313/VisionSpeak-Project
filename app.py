from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication
DB_NAME = 'vision_logs.db'

# Function to save a new log entry
def log_detection(object_name, language_code):
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute("""
            INSERT INTO logs (timestamp, object_detected, language_used)
            VALUES (?, ?, ?)
        """, (timestamp, object_name, language_code))
        
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Database write error: {e}")
        return False
    finally:
        if conn:
            conn.close()

# API endpoint to receive data from the detection system
@app.route('/api/log_detection', methods=['POST'])
def receive_log():
    data = request.get_json()
    
    if not data or 'object' not in data or 'lang' not in data:
        return jsonify({"message": "Invalid data format"}), 400

    success = log_detection(data['object'], data['lang'])
    
    if success:
        return jsonify({"message": "Log recorded successfully"}), 200
    else:
        return jsonify({"message": "Database error"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=5000)
from flask import Flask, request
from markupsafe import escape
import sqlite3
import os

app = Flask(__name__)

# SECURED: Fetching secret from environment variables
SECRET_API_KEY = os.environ.get("API_KEY", "default-dev-key")

@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    # SECURED: Escaping user input to prevent XSS
    safe_query = escape(query)
    html_response = f"<h1>Search Results for: {safe_query}</h1>"
    
    # SECURED: Using parameterized queries to prevent SQL Injection
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (query,))
    results = cursor.fetchall()
    
    html_response += str(results)
    return html_response

if __name__ == '__main__':
    app.run(debug=False) # SECURED: Debug mode disabled in production

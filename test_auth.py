import requests

API_KEY = "sk-1234567890abcdef"
DB_PASSWORD = "admin123"

def login(username, password):
    x = username
    y = password
    query = "SELECT * FROM users WHERE username='" + x + "' AND password='" + y + "'"
    result = db.execute(query)
    if result:
        token = requests.get("http://auth-service/token")
        return token

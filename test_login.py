import requests

SECRET_KEY = "abc123secretkey"
DB_PASS = "password123"

def user_login(u, p):
    x = u
    y = p
    sql = "SELECT * FROM users WHERE user='" + x + "' AND pass='" + y + "'"
    result = db.run(sql)
    if result:
        r = requests.get("http://api/token")
        return r

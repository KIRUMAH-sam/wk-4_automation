# app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Simple login form template 
login_page = """
<!DOCTYPE html>
<html>
<head>
  <title>Login Demo</title>
</head>
<body>
  <h2>AI in Software Engineering - Login Demo</h2>
  <form method="post">
    <label>Username:</label><br>
    <input type="text" name="username"><br><br>
    <label>Password:</label><br>
    <input type="password" name="password"><br><br>
    <button type="submit">Login</button>
  </form>

  {% if message %}
  <p id="message">{{ message }}</p>
  {% endif %}
</body>
</html>
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '1234':
            message = "Login successful! Welcome to your dashboard."
        else:
            message = "Invalid credentials. Please try again."
    return render_template_string(login_page, message=message)

if __name__ == '__main__':
    app.run(debug=True)

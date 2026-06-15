from flask import Flask, render_template, request

app = Flask(__name__)

# Default route - Login Page load karega
@app.route('/')
def login_page():
    return render_template('login.html')

# Form submit hone ke baad Dashboard open karega
@app.route('/dashboard', methods=['POST'])
def dashboard_page():
    # Login page se name fetch karna
    user_name = request.form.get('userName', 'User')
    return render_template('dashboard.html', name=user_name)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
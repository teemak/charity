from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/more_info')
def more_info():
    return render_template('more_info.html')

@app.route('/help_out')
def help_out():
    return render_template('help_out.html')

@app.route('/login')
def login():
    return render_template('login.html');

@app.route('/account')
def account():
    return render_template('account.html')

if __name__ == "__main__":
    app.run()

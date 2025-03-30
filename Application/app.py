from flask import Flask, redirect  # Import Flask and redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("https://www.google.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
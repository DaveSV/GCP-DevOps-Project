from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<div style=\"text-align: center;\"><h1>Hello from Dave!</h1><p>Welcome to GCP DevOps App.</p><p></p></div>'


if __name__ == "__main__":
    app.run(debug=True)
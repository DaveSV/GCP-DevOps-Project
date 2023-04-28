from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<div><img src="https://user-images.githubusercontent.com/29576337/234991334-d5598f99-09e1-4c49-a31a-c9e3b13c3190.png" alt="DevOps deployment" width="248" height="600"></div><div style=\"text-align: center;\"><h1>Hello from Dave!</h1><p>Welcome to GCP DevOps App.</p><p></p></div>'


if __name__ == "__main__":
    app.run(debug=True)
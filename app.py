from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Kubernetes! This is my custom web app running on k8s."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

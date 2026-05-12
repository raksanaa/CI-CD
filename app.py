from flask import Flask

app = Flask(__nam
            e__)

@app.route('/')
def home():
    return "CI/CD Demo Successful 🚀"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

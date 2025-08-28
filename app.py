from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style='font-family:system-ui; color:#a78bfa'>Web Tachiyomi</h1><p>It works! 🟣</p>"

if __name__ == "__main__":
    app.run(debug=True)

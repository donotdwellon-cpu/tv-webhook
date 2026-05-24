from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN   = "8408773669:AAGZJ_qU6GI5sVwI2dl0mWag-PaysPExfKU"
CHAT_ID = "6125995486"

def send(msg):
    url = "https://api.telegram.org/bot" + TOKEN + "/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

@app.route("/webhook", methods=["POST"])
def webhook():
    msg = request.data.decode("utf-8")
    send(msg)
    return "ok", 200

@app.route("/")
def home():
    return "봇 작동중", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

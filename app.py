from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN   = "8872290494:AAHZQbhkHmj2sjWQhVYUT7KIQscJj4_N3hQ"
CHAT_ID = "409161866"

def send(msg):
    url = "https://api.telegram.org/bot" + TOKEN + "/sendMessage"
    r = requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    print("텔레그램 응답:", r.status_code, r.text)

@app.route("/webhook", methods=["POST"])
def webhook():
    msg = request.data.decode("utf-8")
    print("받은 메시지:", msg)
    send(msg)
    return "ok", 200

@app.route("/")
def home():
    return "봇 작동중", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

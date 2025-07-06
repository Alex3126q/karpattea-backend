from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TOKEN = "7681262781:AAGxI7iWBvkjcDyh9YmXEJpeymo84CV_Jic"
CHAT_ID = "7358254292"  

@app.route("/send", methods=["POST"])
def send_order():
    data = request.form
    msg = f"🛒 Нова заявка на чай:\n👤 {data.get('name')}\n📞 {data.get('phone')}\n🚚 {data.get('delivery')}\n🏠 {data.get('address')}\n📝 {data.get('comment', '')}"
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                  json={"chat_id": CHAT_ID, "text": msg})
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

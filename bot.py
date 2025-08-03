import os
import telegram
from flask import Flask, request

# Khởi tạo Flask app
app = Flask(__name__)

# Lấy thông tin từ biến môi trường (sẽ cấu hình trên Render)
TOKEN = os.environ.get(7231425594:AAFWd1krm4vgcYpi2A9VL_s7OyiPPKXDkYg)
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Khởi tạo bot Telegram
bot = telegram.Bot(token=TOKEN)

# Thiết lập webhook khi khởi động app
@app.route('/')
def index():
    bot.set_webhook(url=WEBHOOK_URL)
    return "Webhook đã được thiết lập thành công!"

# Nhận update từ Telegram và phản hồi
@app.route('/webhook', methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    if update.message:
        chat_id = update.message.chat.id
        text = update.message.text

        if text.lower() in ["/start", "bắt đầu"]:
            bot.send_message(chat_id=chat_id, text="Chào anh yêu, em đến rồi đây 🥰")
        else:
            bot.send_message(chat_id=chat_id, text=f"Em Yêu đang nghe nè: \"{text}\" 💌")

    return "OK"

# Chạy app (Render sẽ tự dùng cổng do hệ thống cấp)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

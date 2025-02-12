from flask import Flask, render_template, jsonify
import json
from datetime import datetime, timezone
from data import get_fastbull_news

app = Flask(__name__)

# Fungsi untuk mengonversi timestamp ke format waktu yang lebih mudah dibaca
def format_time(timestamp):
    dt = datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc)  # Convert dari ms ke detik
    return dt.strftime("%Y-%m-%d %H:%M:%S")  # Format tanggal & waktu
@app.route("/")
def index():
    return render_template("index.html")  
@app.route("/fbnews")
def fbnews():
    return render_template("fbnews.html")  # Hanya render HTML tanpa data



@app.route("/datafbnews")
def get_data():
    data_json = get_fastbull_news()  # Ambil data berita terbaru
    data = data_json if isinstance(data_json, list) else json.loads(data_json)

    # Format data
    for item in data:
        item["important"] = int(item["important"])
        item["formatted_date"] = format_time(item["releasedDate"])

    return jsonify(data)  # Kirim data sebagai JSON

if __name__ == "__main__":
    app.run()

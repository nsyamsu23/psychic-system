import requests
import json
# Fungsi untuk mengambil data dari API dengan parameter yang dapat disesuaikan
def get_fastbull_news(checkImportant=0, pageSize=1000, timestamp=None, includeCalendar=1):
    # URL endpoint API dengan parameter dinamis
    url = f"https://api.fastbull.com/fastbull-news-service/api/getNewsPageByTagIds"
    
    # Parameter yang akan dikirim dalam request
    params = {
        "checkImportant": checkImportant,
        "pageSize": pageSize,
        "timestamp": timestamp if timestamp else "",
        "includeCalendar": includeCalendar
    }

    # Headers yang akan dikirim
    headers = {
        "Langid": "13",
    }

    # Mengirim permintaan ke API
    response = requests.get(url, headers=headers, params=params)
    
    # Memproses respons dari API
    if response.status_code == 200:
        data = response.json()
        if data['code'] == 0:
            # Parsing data dari 'bodyMessage'
            news_data = json.loads(data['bodyMessage'])['pageDatas']
            return news_data
        else:
            return None
    else:
        return None


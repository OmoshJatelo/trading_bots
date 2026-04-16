import requests

BOT_TOKEN = "8678576057:AAFIoaFRmMucprPRwCowVNWgydlR7hqX0Sc"
CHAT_ID = "7845820009"

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message
    })
    print(response.json())

send_alert("🚀 SUCCESS: Your alert system is now working!")
import requests

tele_chatbot_key = "<telegram_chatbot_key>"
url = f"https://api.telegram.org/bot{tele_chatbot_key}/"+"getMe"
response = requests.get(url)
response

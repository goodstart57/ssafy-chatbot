from pprint import pprint as pp
from datetime import datetime
import os
import requests

__token = os.getenv('TELEGRAM_TOKEN')

def sendURL(method, params="", domain=f"http://api.telegram.org/bot{__token}"):
    '''send url to use telegram api
    Keyword Arguments:
        method (str) : type of telegram api
        params (str) : prameters of specific telegram api, you should attach "?" sign (default="")
        domain (str) : domain url (host) of telegram api + own telegram bot token default=f"http://api.telegram.org/bot{token}"
    - - - - - - - - - - -
    Return:
        HttpResponse
    - - - - - - - - - - -
    Example:
        response = sendURL(method="getUpdates", params="")
        print(response)
        print(response.text)
    '''
    response = requests.get(f"{domain}/{method}{params}")
    return response

def getID(token, first_name):
    '''Get id by searching User's First Name
    Keyword Arguments:
        token (string) : own telegram bot api token
        first_name (string) : help to search user id by filtering ids
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Return:
        id (string) : it is used to use telegram api
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Example:
        chat_id = getID(my_token, first_name="JS")
        print(chat_id)
    '''
    chat_id = sendURL(method='getUpdates', domain=f"http://api.telegram.org/bot{token}").json()['result']
    chat_id = list(filter(lambda x: x['first_name']==first_name, map(lambda x: x['message']['from'], chat_id)))[0]['id']
    return chat_id

def sendMessage(token, chat_id, text):
    '''SendMessage to telegram user
    Keyword Arguments:
        chat_id (string) : What you want to send
        text (string) : Message text you want to send
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Return:
        HttpResponse
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Example:
        response = sendMessage(chat_id, f"Hello, it's {datetime.now()}")
        print(response)
        print(response.text)
    '''
    response = sendURL(method="sendMessage", params=f"?chat_id={chat_id}&text={text}", domain=f"http://api.telegram.org/bot{token}")
    return response


chat_id = getID(__token, first_name='JS')
# f"Hello, it's {datetime.now()}").text
pp(sendMessage(__token, chat_id, input()))
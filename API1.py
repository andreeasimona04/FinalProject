from fastapi import FastAPI, Request, Response, status
import requests
import json
from secrets import API_KEY

def get_email_content():
    try:
        response = requests.get(f"https://newsapi.org/v2/everything?q=IT&from=2022-08-25&pageSize=10&page=1&language=en&apiKey={API_KEY}")
    except requests.exceptions.RequestException as err:
        print(err)
    else:
        if response.status_code == 200:
            data = response.json()
        else:
            print(response.content)

    for i in data["articles"]:
        print(i["title"])
        # print(i["description"])
        print(i["url"])

print(get_email_content())



    

        
    
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
            content = []
            for i in data["articles"]:
                content.append((i["title"], i["url"]))
            return content
                
# print(get_email_content())




    

        
    
from fastapi import FastAPI, Request, Response, status
import requests
import json
from secrets import API_KEY

try:
    response = requests.get(f"https://newsapi.org/v2/everything?q=Apple&from=2022-08-20&sortBy=popularity&apiKey={API_KEY}")
except requests.exceptions.RequestException as err:
    print(err)
else:
    if response.status_code == 200:
        data = json.loads(response.content)
        
    
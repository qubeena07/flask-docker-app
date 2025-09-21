import requests
import time

#url of the flask api 
URL = "http://flask-api:8000/health"
Check_interval = 10  # seconds

while True:
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print("API is healthy")
        else:
            print(f"API is unhealthy, status code: {response.status_code}")
    except Exception as e:
        print(f"Error connecting to API: {e}")
    
    time.sleep(Check_interval)
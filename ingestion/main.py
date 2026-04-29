import os
import requests
import json
import time
from confluent_kafka import Producer
from dotenv import load_dotenv 

load_dotenv()

def main():
    print("Ingestion service started...")
    
    # TO DO: Add data source API connection
    api_key = os.getenv("MASSIVE_API_KEY")
    url = f"https://api.massive.com/v3/reference/dividends?apiKey={api_key}"

    while True:
        try:
            response = requests.get(url)
            data = response.json()
            print(f"\n--- Data Received at {time.strftime('%H:%M:%S')} ---")
            print(data, flush=True)
        except Exception as e:
            print(f"Error fetching data: {e}", flush=True)

        time.sleep(15)

    # TO DO: Add redpanda connection
    
    pass

if __name__ == "__main__":
    main()
import os
import requests
import json
import time
from confluent_kafka import Producer
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Ingestion service started...")

    # get credentials from .env
    api_key = os.getenv("MASSIVE_API_KEY")
    kafka_broker = os.getenv("KAFKA_BROKER")

    # build the API url
    url = "https://api.massive.com/v3/reference/dividends"
    url = url + "?apiKey=" + api_key

    # connect to redpanda
    producer_config = {"bootstrap.servers": kafka_broker}
    producer = Producer(producer_config)

    while True:
        # fetch data from API
        print(f"\n--- Fetching data at {time.strftime('%H:%M:%S')} ---")
        response = requests.get(url, timeout=10)
        data = response.json()
        results = data["results"]
        print(f"Got {len(results)} dividends from API")

        # send each dividend to redpanda one at a time
        for dividend in results:
            ticker = dividend["ticker"]
            message = json.dumps(dividend)

            print(f"Sending {ticker} to redpanda...")
            producer.produce(
                topic="dividends",
                key=ticker,
                value=message
            )

        # actually send all the messages
        producer.flush()
        print("All messages sent to redpanda")

        # wait 15 seconds before fetching again
        print("Waiting 15 seconds...")
        time.sleep(15)

if __name__ == "__main__":
    main()
import os
from confluent_kafka import Consumer
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Processing service started...")
    
    # TO DO: Add connection to redpanda

    # TO DO: Add processing / prediction logic

    # TO DO: Add connection to postgres 

    pass

if __name__ == "__main__":
    main()
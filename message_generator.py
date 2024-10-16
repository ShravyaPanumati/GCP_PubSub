import os
import random
import time
from google.cloud import pubsub_v1

GOOGLE_APPLICATION_CREDENTIALS_PATH = "E:\strategic-reef-435523-j1-b63447c13134.json"  # Path to your service account JSON file

# Set the environment variable for Google Application Credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS_PATH

# Initialize Pub/Sub client
project_id = 'strategic-reef-435523-j1'  # Replace with your Google Cloud project ID
topic_name = 'my-topic'  # Replace with your Pub/Sub topic name
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

# List of quotes to publish
quotes = [
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Get busy living or get busy dying. - Stephen King",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "Believe you can and you're halfway there. - Theodore Roosevelt"
]

def publish_quote():
    # Limit to 5 quotes
    for _ in range(5):
        # Randomly select a quote
        quote = random.choice(quotes)

        # Publish the quote to Pub/Sub
        future = publisher.publish(topic_path, quote.encode('utf-8'))
        print(f'Published: {quote}')

        # Wait for a few seconds before publishing the next quote
        time.sleep(5)

if __name__ == '__main__':
    publish_quote()

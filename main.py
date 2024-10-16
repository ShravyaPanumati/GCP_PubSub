import os
import pyodbc
from google.cloud import pubsub_v1


GOOGLE_APPLICATION_CREDENTIALS_PATH = "E:\strategic-ref-435523-j2-b63447c14314.json"  # Replace with your json file of service account

# Set the environment variable for Google Application Credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS_PATH

# Database connection function
def connect_db():
    # Database connection details
    server = ''  # Replace with your instance public IP of database in GCP
    database = 'myappdb'  # Replace with your database name
    username = 'myuser'  # Get username from environment variable
    password = ''  # Replace with your password
    driver = '{ODBC Driver 17 for SQL Server}'  # ODBC driver

    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    return pyodbc.connect(connection_string)


# Callback function to handle incoming messages
def callback(message):
    print(f'Received message: {message.data.decode("utf-8")}')

    # Store the message in the database
    store_message_in_db(message.data.decode('utf-8'))

    # Acknowledge the message
    message.ack()


def store_message_in_db(quote):
    conn = connect_db()
    cursor = conn.cursor()

    # Insert the quote into the database
    cursor.execute("INSERT INTO Quotes (QuoteText) VALUES (?)", (quote,))
    conn.commit()
    cursor.close()
    conn.close()
    print(f'Stored in database: {quote}')


def main():
    # Initialize Pub/Sub subscriber
    project_id = 'strategic-reef-435523-j1'  # Replace with your Google Cloud project ID
    subscription_name = 'my-topic-sub'  # Replace with your Pub/Sub subscription name
    topic_name = 'my-topic'
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    # Start listening for messages
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f'Listening for messages on {subscription_path}...')

    try:
        streaming_pull_future.result()
    except KeyboardInterrupt:
        streaming_pull_future.cancel()


if __name__ == '__main__':
    main()

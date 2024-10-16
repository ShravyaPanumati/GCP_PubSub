Google Cloud Pub/Sub is a fully-managed real-time messaging service that allows you to send and receive messages between independent applications. It is part of the Google Cloud Platform (GCP) and is designed to provide reliable, many-to-many asynchronous messaging between applications.

Core concepts in Pub/Sub are:

Publisher: An application that sends messages to a topic.

Subscriber: An application that receives messages from a subscription.

Topic: A named resource to which messages are sent by publishers.

Subscription: A named resource that represents the stream of messages from a specific topic. Subscribers receive messages from this subscription.

The Workflow of Pub/Sub is as follows:

Publish Messages: A publisher sends messages to a specified topic.

Receive Messages: Subscribers pull messages from a subscription attached to that topic.

message_generator.py is the python code file which generates the random messages. In this case, I had used random quotes i.e.., publishing messages.
Install pubsub library using the command "pip install google-cloud-pubsub"
Create a pubsub topic using the command "gcloud pubsub topics create my-topic-name"
Provide the topic name and project id in the message_generator.py

main.py is the python code which receives the message as a subscriber/subscription and then pushes the message into a database
In this code we will specify the project id, database credentials and susbscription name for the topic created while publishing. The subscription name can be created as follows utilizing the topic with the command "gcloud pubsub subscriptions create my-sub --topic=my-topic".
The code will send the received messages to the database.

Run message_generator.py file using the command "python message_generator.py" which will publish the message.
Then run main.py using "python main.py" and check the logs whther it has been received and stored in the database provided in the code.
The output is as follows:
![image](https://github.com/user-attachments/assets/d5a43c77-3dd2-487c-88ad-d2e1978814ab)

 


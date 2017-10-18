# Created by Omer Shwartz (www.omershwartz.com)
#
# This script uses service credentials to subscribe to a topic of the Pub/Sub broker residing in
# Google Cloud.
# Using this code a server can receive messages from the device.
#
# This file may contain portions of cloudiot_mqtt_example.py licensed to Google
# under the Apache License, Version 2.0. The original version can be found in
# https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/iot/api-client/mqtt_example/cloudiot_mqtt_example.py
#
############################################################

import time
import os

from google.cloud import pubsub
from oauth2client.service_account import ServiceAccountCredentials

project_id = 'awesome-project-31'  # Enter your project ID here
topic_name = 'my_device_events'  # Enter your topic name here
subscription_name = 'my_subscription'  # Can be whatever, but must be unique (for the topic?)
service_account_json = 'service_account.json' # Location of the server service account credential file


def on_message(message):
    """Called when a message is received"""
    print('Received message: {}'.format(message))
    message.ack()


# Ugly hack to get the API to use the correct account file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_json

# Create a pubsub subscriber
subscriber = pubsub.SubscriberClient()

topic = 'projects/{project_id}/topics/{topic}'.format(
    project_id=project_id,
    topic=topic_name,
)

subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
    project_id=project_id,
    sub=subscription_name,
)

# Try to delete the subscription before creating it again
try:
    subscriber.delete_subscription(subscription_name)
except: # broad except because who knows what google will return
    # Do nothing if fails
    None

# Create subscription
subscription = subscriber.create_subscription(subscription_name, topic)

# Subscribe to subscription
print "Subscribing"
subscriber.subscribe(subscription_name, callback=on_message)

# Keep the main thread alive
while True:
    time.sleep(100)

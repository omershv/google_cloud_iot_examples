# Google Cloud IoT Examples
In here there are scripts that allow full bi-directional communication between an IoT device and a server through Google Cloud brokering.


# mqtt_publisher.py
# -----------------
This script uses device credentials to publish events to the MQTT broker residing in Google Cloud.
Using this code a device can 'talk' to the server.

# mqtt_state_subscriber.py
# -----------------
This script uses device credentials to subscribe to the device configuration topic of the MQTT broker residing in Google Cloud.
Using this code a device can receive configuration from the server.

# pubsub_subscriber.py
# -----------------
This script uses service credentials to subscribe to a topic of the Pub/Sub broker residing in Google Cloud.
Using this code a server can receive messages from the device.

# set_device_configuration.py
# -----------------
This script uses service credentials to modify device configuration over REST API of Google Cloud.
Using this code a server can change the configuration of the device.

# This files in this repository may contain portions of cloudiot_mqtt_example.py licensed to Google
# under the Apache License, Version 2.0. The original version can be found in
# https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/iot/api-client/mqtt_example/cloudiot_mqtt_example.py

from scholarly import scholarly
import json
from confluent_kafka import Producer, KafkaException
import paho.mqtt.client as mqtt
#------------------------------------------FUNCTION------------------------------------------
def write_json(path: str,json_str: str):
    with open(path, "w") as outfile:
            outfile.write(json_str)
def send_to_kafka_topic(data):
    topic = "publication"
    bootstrap_servers = "192.168.107.137"
    producer_conf = {
        'bootstrap.servers': bootstrap_servers
    }
    producer = Producer(producer_conf)
    try:
        # Convert dictionary to JSON string
        json_data = json.dumps(data)
        # Produce the message to the Kafka topic
        producer.produce(topic, key=None, value=json_data)
        # Flush the producer to ensure the message is sent
        producer.flush()
        print("Message sent successfully.")
    except KafkaException as e:
        print("Failed to send message to Kafka: {}".format(e))
def publish_dict_to_mqtt(dict_data, topic):
    # Convert the dictionary to a JSON string
    json_payload = json.dumps(dict_data)

    # Connect to the MQTT broker
    client = mqtt.Client()
    client.connect("192.168.107.137", 1883)  # Replace with your MQTT broker address

    # Publish the JSON payload to the specified topic
    client.publish(topic, payload=json_payload)

    # Disconnect from the MQTT broker
    client.disconnect()
def getPublication(author_name):
    #------------------------------------------FUNCTION------------------------------------------
    # Retrieve the author's data, fill-in, and print
    # Get an iterator for the author results
    search_query = scholarly.search_author(author_name)
    # Retrieve the first result from the iterator
    first_author_result = next(search_query)
    #scholarly.pprint(first_author_result)
    # Retrieve all the details for the author
    author = scholarly.fill(first_author_result )
    #scholarly.pprint(author)
    publications = author['publications']
    publications_dict = {}
    for i in range(len(publications)):
        publications_dict[i]=publications[i]
    return publications_dict
def getAuthorInformation(author_id):
    author_info = scholarly.search_author_id(author_id)
    return author_info
#------------------------------------------FUNCTION------------------------------------------
# author_name = "Lam Tran Thanh Nguyen"
# search_query = scholarly.search_author(author_name)
# first_author_result = next(search_query)
# author = scholarly.fill(first_author_result )
# publications = author['publications']
# publications_dict = {}
# for i in range(len(publications)):
#     print("--------------------------Loop i ="+str(i)+"--------------------------")
#     print(publications[i])
#     publications_dict[i]=publications[i]
# filename = author_name.replace(" ", "-")
# write_json("publication-"+filename+".json",json.dumps(publications_dict))
# #Send to kafka
# #send_to_kafka_topic(publications_dict)
# #send to MQTT
# publish_dict_to_mqtt(publications_dict, "publication")
id = "Yt6EcJYAAAAJ"
author_name = str(getAuthorInformation(id)["name"])
publication = getPublication(author_name)
print(publication)
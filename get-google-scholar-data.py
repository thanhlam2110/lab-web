from scholarly import scholarly
import json
from confluent_kafka import Producer, KafkaException
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
    # finally:
    #     producer.close()
#------------------------------------------FUNCTION------------------------------------------
# Retrieve the author's data, fill-in, and print
# Get an iterator for the author results
author_name = "Lam Tran Thanh Nguyen"
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
    print("--------------------------Loop i ="+str(i)+"--------------------------")
    print(publications[i])
    publications_dict[i]=publications[i]
filename = author_name.replace(" ", "-")
write_json("publication-"+filename+".json",json.dumps(publications_dict))
send_to_kafka_topic(publications_dict)

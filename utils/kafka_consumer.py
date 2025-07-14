import logging
from threading import Event
from multiprocessing import Queue

from flask import Flask
from models.proto.wikipost_pb2 import WikiPost
from confluent_kafka.deserializing_consumer import DeserializingConsumer
from confluent_kafka.serialization import StringDeserializer
from confluent_kafka.schema_registry.protobuf import ProtobufDeserializer

# from utils.event_queue import kafka_eq
from models.dto.event_queue_dto import EventQueueItem as eq_item


def create_consumer(app:Flask, kafka_eq:Queue, stop_event:Event):

    schema_registry_conf = {'url': app.config['KAFKA_SCHEMA_REGISTRY_URL']}

    protobuf_deserializer = ProtobufDeserializer(WikiPost, schema_registry_conf)

    string_deserializer = StringDeserializer('utf_8')

    c = DeserializingConsumer({
        'bootstrap.servers': app.config['KAFKA_BROKER_URL'],
        'group.id': 'wiki-group-1',
        'auto.offset.reset': 'earliest',
        'key.deserializer': string_deserializer,
        'value.deserializer': protobuf_deserializer,
    })

    c.subscribe(['lesson_demo1'])

    logging.info('Entering polling loop...')
    try:
        while not stop_event.is_set():
        # while True:
            msg = c.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                logging.error('Consumer error', msg.error())
                continue
            
            user_obj = msg.value()

            new_item = eq_item(msg.key(), user_obj.SerializeToString())

            kafka_eq.put(new_item)
            # logging.info(f'Putting into queue: {new_item}')
    except Exception as err:
        logging.error('Error when polling', err)
    finally:
        try:
            # Only commit if there are positions (offsets) to commit
            assigned_partitions = c.assignment()

            # Check if any positions are known for those partitions
            if assigned_partitions:
                is_commit = False
                for partition in assigned_partitions:
                    pos = c.position([partition])
                    if pos and pos[0].offset >= 0:
                        is_commit = True
                        break

                if is_commit:
                    logging.info("Committing offsets manually before shutdown...")
                    c.commit()
                else:
                    logging.info("No offsets to commit. Skipping commit.")
            else:
                logging.info("No partitions assigned. Skipping commit.")

        except Exception as e:
            logging.warning(f"Manual offset commit failed: {e}")
        c.close()
        logging.info('Consumer thread gracefully shutting down...')

    logging.info('Consumer thread shutdown completed.')

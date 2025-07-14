import queue
from threading import Event
import logging
from flask import Flask

from utils.event_queue import kafka_eq
from service.kafka_svc import KafkaService as kafka_svc


def process(app:Flask, stop_event:Event):
    # Injecting context to setup db connection
    with app.app_context():
        try:
            while not stop_event.is_set():
                try:
                    item = kafka_eq.get(timeout=1)
                    logging.info('Retrieving event...')
                    event = kafka_svc().save(item.key, item.value)
                    logging.info(f'Saved event of id {event.id}...')
                except queue.Empty:
                    pass
                except Exception as err:
                    logging.error('Error when processing event queue', err)
        finally:
            logging.info('Event queue thread gracefully shutting down...')
    
        logging.info('Event queue thread shutdown completed.')
    
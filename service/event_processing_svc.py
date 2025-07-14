import queue
import logging
from multiprocessing import Queue
from multiprocessing.synchronize import Event
from flask import Flask

from models.proto.wikipost_pb2 import WikiPost
# from utils.event_queue import kafka_eq
from service.kafka_svc import KafkaService as kafka_svc


def process_run(kafka_eq:Queue, stop_event:Event):
    # Create app context for new process
    from app_factory import create_app
    curr_app = create_app()

    logging.info('Starting event process...')
    try:    
        while not stop_event.is_set():
            with curr_app.app_context():
                try:
                    item = kafka_eq.get(timeout=1)
                    new_post = WikiPost()
                    new_post.ParseFromString(item.value)
                    event = kafka_svc().save(item.key, new_post)
                    logging.info(f'Saved event of id {event.id}...')
                except queue.Empty:
                    pass
                except Exception as err:
                    logging.error('Error when processing event queue', err)
    except KeyboardInterrupt:
        logging.info('Signal sigint detected...')
    except Exception as err:
        logging.error('Error when stopping event process.', err)
    finally:
        logging.info('Event queue thread gracefully shutting down...')
    
    logging.info('Event queue thread shutdown completed.')

def thread_run(app:Flask, kafka_eq:Queue, stop_event):
    # Injecting context to setup db connection
    with app.app_context():
        try:
            while not stop_event:
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
    
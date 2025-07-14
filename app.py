import logging
import threading

from utils.kafka_consumer import create_consumer
from service.event_processing_svc import process
from app_factory import create_app
from utils.signal_setup import setup_signal_handlers, stop_flag

app = create_app()

logging.info('Starting consumer from main app...')
consumer_thread = threading.Thread(
    target=create_consumer,
    args=(app, stop_flag),
)

logging.info('Starting processing loop...')
event_queue_thread = threading.Thread(
    target=process,
    args=(app, stop_flag),
)

setup_signal_handlers(consumer_thread, event_queue_thread)

consumer_thread.start()
event_queue_thread.start()

if __name__ == "__main__":
    
    try:
        app.run(use_reloader=False)
    finally:
        stop_flag.set()

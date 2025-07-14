import logging
import threading
import multiprocessing

from utils.kafka_consumer import create_consumer
from service.event_processing_svc import process_run
from app_factory import create_app
from utils.signal_setup import setup_signal_handlers, stop_thread_flag, stop_process_flag
from utils.event_queue import kafka_eq

app = create_app()

curr_threads = []
logging.info('Starting consumer from main app...')
consumer_thread = threading.Thread(
    target=create_consumer,
    args=(app, kafka_eq, stop_thread_flag, ),
)
curr_threads.append(consumer_thread)

curr_processes = []
logging.info('Starting processing loop...')
event_process_thread = multiprocessing.Process(
    target=process_run,
    args=(kafka_eq, stop_process_flag, ),
)
curr_processes.append(event_process_thread)

setup_signal_handlers(curr_threads, curr_processes)

for curr_thread in curr_threads:
    curr_thread.start()

for curr_process in curr_processes:
    curr_process.start()

if __name__ == "__main__":
    
    try:
        app.run(use_reloader=False)
    finally:
        stop_thread_flag.set()
        stop_process_flag.set()

import signal
import logging
import sys
from threading import Event, Thread

# Shared shutdown flag
stop_flag = Event()

def setup_signal_handlers(consumer_thread:Thread, event_thread:Thread):
    def handle_signal(sig, frame):
        logging.info(f"Signal {sig} received, stopping gracefully...")
        stop_flag.set()
        consumer_thread.join()
        event_thread.join()
        logging.info(f"Joining threads...")
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)
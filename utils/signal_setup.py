import signal
import logging
import sys
import multiprocessing
import threading
from threading import Thread
from multiprocessing import Process
from typing import List

# Shared shutdown flag
stop_thread_flag = threading.Event()
stop_process_flag = multiprocessing.Event()

def setup_signal_handlers(threads:List[Thread], processes:List[Process]):
    def handle_signal(sig, frame):
        logging.info(f"Signal {sig} received, stopping gracefully...")

        stop_thread_flag.set()
        stop_process_flag.set()

        for curr_thread in threads:
            curr_thread.join()
        logging.info(f"Joining threads completed.")

        for curr_process in processes:
            curr_process.terminate()
            curr_process.join()
        logging.info(f"Terminating and joining processes completed.")
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

class Watcher:
    DIRECTORY_TO_WATCH = "./toWatch"  # Replace with the path to the directory you want to watch

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # When a file is created
            logging.info(f"Received created event - {event.src_path}.")

        elif event.event_type == 'modified':
            # When a file is modified
            logging.info(f"Received modified event - {event.src_path}.")

        elif event.event_type == 'deleted':
            # When a file is deleted
            logging.info(f"Received deleted event - {event.src_path}.")

if __name__ == '__main__':
    logging.basicConfig(filename='file_change_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    w = Watcher()
    w.run()

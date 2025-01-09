import threading
from datetime import datetime


class Timer:
    def __init__(self, interval, callback):
        self.interval = interval
        self.callback = callback
        self.thread = threading.Timer(self.interval, self._callback_wrapper)
        self.thread.start()

    def _callback_wrapper(self):
        last_time = float(datetime.timestamp(datetime.utcnow()))
        self.callback()
        elapsed = float(datetime.timestamp(datetime.utcnow())) - last_time
        sleep_for = self.interval - elapsed
        self.thread = threading.Timer(sleep_for, self._callback_wrapper)
        self.thread.start()

    def stop(self):
        self.thread.cancel()


def example_callback():
    curr_time = float(datetime.timestamp(datetime.utcnow()))
    print("Callback called at: ", curr_time)


if __name__ == "__main__":
    r = Timer(1.0, example_callback)
    try:
        while True:
            pass
    except KeyboardInterrupt:
        r.cancel()
        print("Timer stopped")

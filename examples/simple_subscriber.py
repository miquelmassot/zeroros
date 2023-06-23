import time

from zeroros import Subscriber
from zeroros.messages import String


def callback(msg: String):
    print("Received message:\n", msg)


def main():
    sub = Subscriber("/test_topic", String, callback)  # noqa: F841
    print("Subscribing to /test_topic")
    print("Press Ctrl+C to stop.")
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()

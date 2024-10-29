import asyncio
import json
import time
import sys

import zmq

from zeroros.messages import Header, Message
from zeroros.topic import validate_topic


if sys.platform == 'win32':
   asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class Publisher:
    def __init__(
        self,
        topic: str,
        message_class: type[Message],
        ip: str = "127.0.0.1",
        port: int = 5555,
        verbose: bool = False,
    ):
        if verbose:
            print("Creating publisher for topic: ", topic)
        self.topic = validate_topic(topic)
        self.message_class = message_class
        self.ip = ip
        self.port = port
        self.context = zmq.Context()
        self.sock = self.context.socket(zmq.PUB)
        try:
            self.sock.connect("tcp://" + str(self.ip) + ":" + str(self.port))
        except Exception as e:
            print("Exception: ", e)
            raise e

    def publish(self, message):
        # Check message is of the correct type
        if not isinstance(message, self.message_class):
            raise TypeError(f"Message must be of type {self.message_class.__name__}")
        message_str = json.dumps(message.to_json())
        topic_message_str = f"{self.topic} {message_str}"
        message_bytes = topic_message_str.encode("utf-8")
        self.sock.send(message_bytes)


if __name__ == "__main__":
    pub = Publisher("/header", Header)
    msg = Header()
    while True:
        msg.stamp = time.time()
        pub.publish(msg)
        msg.seq += 1
        time.sleep(0.5)

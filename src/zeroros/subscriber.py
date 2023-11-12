import asyncio
import json
import threading
import time
import sys

import zmq
import zmq.asyncio

from zeroros.messages import Header, Message
from zeroros.topic import validate_topic


if sys.platform == 'win32':
   asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class Subscriber:
    def __init__(
        self,
        topic: str,
        message_class: type[Message],
        callback_handle: callable,
        ip: str = "127.0.0.1",
        port: int = 5556,
        verbose: bool = False,
    ):
        self.ip = ip
        self.port = port
        self.verbose = verbose
        if self.verbose:
            print("Subscribing to topic: ", topic)
        self.topic = validate_topic(topic)
        self.message_class = message_class
        self.url = "tcp://" + str(self.ip) + ":" + str(self.port)
        self.context = zmq.asyncio.Context()
        self.msg = self.message_class()
        self._stop = False
        self.listening_thread = threading.Thread(
            target=self.listen, args=(callback_handle,), daemon=True
        )
        self.listening_thread.start()

    def stop(self):
        self._stop = True

    def listen(self, callback_handle: callable):
        while not self._stop:
            try:
                self.msg = self.message_class()
                # create a task
                asyncio.run(self.recv_and_process())
                # register a done callback function
                callback_handle(self.msg)
            except Exception as e:
                print(f"Error for topic {self.topic} on {self.ip}:{self.port}: {e}")
            time.sleep(0.05)
        if self.verbose:
            print("Stopping subscriber")
        # Check if the socket is still open
        if self.sock.closed is False:
            self.sock.close()
        self.context.term()

    async def recv_and_process(self):
        self.sock = self.context.socket(zmq.SUB)
        self.sock.setsockopt(zmq.SUBSCRIBE, str.encode(self.topic))
        self.sock.connect(self.url)
        received_msg = await self.sock.recv()
        self.sock.close()
        # Split the message into topic and message
        topic, message = received_msg.split(b" ", 1)
        # Check that the topic is correct
        if topic.decode("utf-8") != self.topic:
            raise ValueError(
                f"Topic received ({topic.decode('utf-8')})"
                f" does not match expected topic ({self.topic})"
            )
        try:
            # Decode the message
            message = message.decode("utf-8")
            # Parse the message
            message = json.loads(message)
            # Create a message object
            self.msg.from_json(message)
        except Exception as e:
            raise ValueError(f"Could not decode message: {e}")


if __name__ == "__main__":

    def callback(msg):
        print("Received in callback:", msg)

    sub = Subscriber("/header", Header, callback)
    while True:
        time.sleep(1)

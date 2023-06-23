import threading

import zmq


class MessageBroker:
    def __init__(self):
        # gather list of topics from pub/subs
        self.topics = {}
        # run broker in seperate thread
        self.broker_thread = threading.Thread(target=self.config_broker)
        self.broker_thread.start()

    def config_broker(self):
        """connects, binds, and configure sockets"""
        # https://zguide.zeromq.org/docs/chapter2/#The-Dynamic-Discovery-Problem
        self.context = zmq.Context()
        frontend = self.context.socket(zmq.XSUB)
        frontend.bind("tcp://127.0.0.1:5559")
        backend = self.context.socket(zmq.XPUB)
        backend.bind("tcp://127.0.0.1:5560")

        # built-in pub/sub fowarder
        zmq.proxy(frontend, backend)

        # Shouldn't get here
        frontend.close()
        backend.close()
        self.context.term()


if __name__ == "__main__":
    MessageBroker()

import threading

import zmq


class MessageBroker:
    def __init__(self, ip="127.0.0.1", xsub_port=5555, xpub_port=5556):
        # gather list of topics from pub/subs
        self.topics = {}
        self.context = None
        self.ip = ip
        self.xsub_port = xsub_port
        self.xpub_port = xpub_port
        # run broker in separate thread
        self.broker_thread = threading.Thread(target=self.config_broker)
        self.broker_thread.start()

    def config_broker(self):
        """connects, binds, and configure sockets"""
        # https://zguide.zeromq.org/docs/chapter2/#The-Dynamic-Discovery-Problem
        try:
            self.context = zmq.Context()
            frontend = self.context.socket(zmq.XSUB)
            frontend.bind("tcp://" + str(self.ip) + ":" + str(self.xsub_port))
            backend = self.context.socket(zmq.XPUB)
            backend.bind("tcp://" + str(self.ip) + ":" + str(self.xpub_port))

            # built-in pub/sub fowarder
            zmq.proxy(frontend, backend)
        except zmq.error.ContextTerminated:
            print("Context terminated")
        except Exception as e:
            print("Error: ", e)
        finally:
            frontend.close()
            backend.close()

    def stop(self):
        self.context.term()


if __name__ == "__main__":
    MessageBroker()

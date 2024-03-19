import threading
import time

class Buffer:
    def __init__(self):
        self.semaphore = threading.Semaphore(0)
        self.items = []

    def produce(self, item):
        print("Producing", item)
        self.items.append(item)
        self.semaphore.release()

    def consume(self):
        self.semaphore.acquire()
        item = self.items.pop(0)
        print("Consuming", item)

def producer(buffer):
    for i in range(5):
        buffer.produce(i+1)
        time.sleep(1)

def consumer(buffer):
    for i in range(5):
        buffer.consume()
        time.sleep(1)

buffer = Buffer()
producer_thread = threading.Thread(target=producer, args=(buffer,))
consumer_thread = threading.Thread(target=consumer, args=(buffer,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
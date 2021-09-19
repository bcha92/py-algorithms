# Ticket Queue

import time
import random

class Queue:
    def __init__(self):
        self.items = []
    # Returns True if queue is empty
    def is_empty(self):
        return "Is the queue empty? {}".format(self.items == [])
    # Adds item to the queue
    def enqueue(self, item):
        self.items.insert(0, item)
    # Removes item from the queue
    def dequeue(self):
        self.items.pop()
    # Returns the length of this queue
    def size(self):
        return "There are {} items in this queue.".format(len(self.items))
    # Line Simulation
    def simulate_line(self, till_show, max_time):
        pq = Queue()
        tix_sold = []
        for i in range(100):
            pq.enqueue("guest#" + str(i))
            t_end = time.time() + till_show
            now = time.time()
            while now < t_end and not pq.is_empty():
                now = time.time()
                r = random.randint(0, max_time)
                time.sleep(r)
                person = pq.dequeue()
                print(person)
                tix_sold.append(person)
            return tix_sold

# Sample Value Input
print(time)
queue = Queue()
sold = queue.simulate_line(5, 1)
print(sold)

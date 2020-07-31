import time
import queue
import logging
from multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def deposit(namespace, lock):
    for _ in range(1, 100000):

        lock.acquire()
        namespace.balance += 1
        lock.release()

def withdraw(namespace, lock):
    for _ in range(1, 100000):
        with lock:
            namespace.balance -= 1

if __name__ == "__main__":
    manager = multiprocessing.Manager()

    lock = manager.Lock()

    namespace = manager.Namespace()
    namespace.balance = 0

    proccess1 = multiproccesing.Process(target=deposit, args=(namespace, lock))
    proccess2 = multiproccesing.Process(target=withdraw, args=(namespace, lock))

    proccess1.start()
    proccess2.start()

    proccess1.join()
    proccess2.join()

    logging.info(f'Valor balance final es: {namespace.balance}')
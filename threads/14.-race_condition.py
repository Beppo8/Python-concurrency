import time
import logging
import threading
import requests

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

#RACE CONDITION

BALANCE = 0

lock = threading.Lock()

def depositos():
    global BALANCE

    for _ in range(0, 10000):
        with lock:
            BALANCE += 1 # Seccion critica

def retiros():
    global BALANCE

    for _ in range(0, 10000):
        try:
            lock.acquire()
            BALANCE -= 1
        finally:
            lock.release()

if __name__ == "__main__":
    tread1 = treading.Thread(target=depositos)
    thread2 = threading.Thread(target=retiros)

    threadin1.start()
    threadin2.start()

    threadin1.join()
    threadin2.join()

    logging.info(f'El valor final del balance es: {BALANCE}')
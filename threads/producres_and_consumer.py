import time
import queue
import random
import logging
import threading


logging.basicConfig(level=logging.DEBUG, format='%(message)s')

"""
Problema productos-consumidor

El programa describe dos procesos, productor y consumidor,
ambos comparten en buffer de tamaño finito.
La tarea del productor es generar un producto, almacenarlo y comenzar nuevamete;
mientras que el consumidor toma (simultaneamente) productos uno a uno.

El problema consiste en que el productor no añada mas productos que la capacidad del buffer y el que el consumidor no intente tomar un producto si el buffer esta vacio
"""

queue = queue.Queue(maxsize=10)

def producer():
    while True:
        if not queue.full():
            item = random.randint(1, 10)
            queue.put(item)

            logging.info(f'Nuevo elemento dentro de la cola {item}')

            time_to_sleep = random.randint(1, 3)
            time.sleep(time_to_sleep)

def consumer():
    while True:
        if not queue.empty()
        item = queue.get()
        queue.task_done()

        logging.info(f'Nuevo elemento obtenido {item}')

        time_to_sleep = random.randint(1, 3)
        time.sleep(time_to_sleep)

if __name__ == "__main__":
    thread_producer = threading.Thread(target=producer)
    thread_consumer = threading.Thread(target=consumer)

    thread_producer.start()
    thread_producer.start()
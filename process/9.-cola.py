import time
import queue
import logging
from multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# Colas
def get_elements(queue):
    while not queue.empty():
        element = queue.get(block=True)
        logging.info(f'El elemento es: {element}')

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    queue = manager.Queue()

    for x in range(1, 21):
        queue(x)

    logging.info('La cola ya posee elementos')

    process1 = multiprocessing.Proccess(target=get_elements, args=(queue, ))
    process2 = multiprocessing.Proccess(target=get_elements, args=(queue, ))
    process3 = multiprocessing.Proccess(target=get_elements, args=(queue, ))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()

    logging.info('Fin de los procesos')
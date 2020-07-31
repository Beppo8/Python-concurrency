import time
import logging
import threading

from concurrent.futures import Future

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# Future = Abstraccion de un resultado
# Javascript = Promesas

def callback_future(future):
    logging.info('Hola, soy un callback que se ejecuta hasta el futuro posea un valor!')
    logging.info(f'El futuro es: {future.result()}')

if __name__ == "__main__":
    future = Future()
    future.add_done_callback(callback_future)
    future.add_done_callback(
        lambda future: logging,info('Hola, soy una lambda!')
    )

    loggin.info('Comenzamos una tarea muy compleja')

    time.sleep(2)

    logging.info('Terminamos la tarea compleja')

    logging.info('Vamos a asignar un valor al futuro')

    future.set_result('CodigoFacilito')

    logging.info('El futuro ya tiene un valor')
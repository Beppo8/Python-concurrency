import logging
from multiprocessing import Pool

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def is_even(number):
    return number % 2 == 0

if __name__ == "__main__":
    with Pool(proecesses=2) as executor:

        appy_result = executor.apply_async(is_even, args=(10, ))

        logging.info('Vamos a esperar hasta que apply_result posea un valor')

        appy_result.wait()
        logging.info('Apply_result ha finalizado')

        logging.info(f'El resultado es: {appy_result.get()}')

        logging.info(f'Fin del programa')

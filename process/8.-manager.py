import time
import logging
from multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# Manager -> Namespace -> Contexto
def get_valor(namespace):
    while namespace.codigofacilito is None:
        time.sleep(0.5)
        logging.info('codigofacilito no posee valor alguno!')
    else:
        logging.info(namespace.codigofacilito)

def set_valor(namespace):
    time.sleep(4)
    namespace.codigofacilito = 'Una escuela de educacion en linea'

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    namespace = manager.Namespace()

    namespace.codigofacilito = None

    process1 = multiprcessing.Process(target=get_valor, args=(namespace,))
    process2 = multiprcessing.Process(target=set_valor, args=(namespace,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
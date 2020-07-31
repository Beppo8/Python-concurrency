import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def thread_1(event):
    logging.info('Hola, soy el thread numero uno')

    event.wait()

    logging.info('La señal fue dada, la bandera es True')

def thread_2(event):
    
    while not event.is_set():
        logging.info('A la espera de la señal')
        time.sleep(0.5)

def show_user_name():
    name = user.get('name').get('first')

    logging.info(f'El nombre del usuario es: {name}')


if __name__ == "__main__":
    
    event = threading.Event()
    #Bandera = True o False

    thread1 = threading.Thread(target=thread_1, args=(event, ))
    thread2 = threading.Thread(target=thread_2, args=(event, ))

    thread1.start()
    thread2.start()

    time.sleep(3)

    event.set()
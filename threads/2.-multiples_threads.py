import threading

def executor_a(id=0):
    for x in range(0, 10):
        print(f'Hola, soy el Thread {id} iteracion {x}')

def executor_b():
    for x in range(0, 10):
        print(f'Hola, soy el Thread {id} iteracion {x}')

def executor_c():
    for x in range(0, 10):
        print(f'Hola, soy el Thread {id} iteracion {x}')

thread_a = threading.Thread(target=executor_a, args=[1])
thread_b = threading.Thread(target=executor_b, args=(2,))
thread_c = threading.Thread(target=executor_c, kwargs={'id': 3})

thread_a.start()
thread_b.start()
thread_c.start()
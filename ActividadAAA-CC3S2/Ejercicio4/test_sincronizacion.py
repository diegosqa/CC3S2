import threading
from sincronizacion import Contador

def test_incremento_con_hilos():
    contador = Contador()
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=contador.incrementar, args=(100,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    assert contador.valor == 1000, f"Se esperaba 1000, pero se obtuvo {contador.valor}"

def test_sin_condiciones_de_carrera():
    contador = Contador()
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=contador.incrementar, args=(100,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    assert contador.sin_condiciones_carrera(), "Se detectó una condición de carrera."


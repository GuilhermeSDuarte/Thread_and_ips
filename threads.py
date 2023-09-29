from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        time.sleep(0.5)
        trajeto += velocidade
        print('Carro: {} km: {}\n' .format(piloto, trajeto))

thread_carro1 = Thread(target=carro, args=[3, 'Piloto1'])
thread_carro2 = Thread(target=carro, args=[5, 'Piloto2'])

thread_carro1.start()
thread_carro2.start()

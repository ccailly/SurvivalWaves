import j2l.pytactx.agent as pytactx
from time import sleep 
from random import randint
from Zombie import Zombie
import time
from Referee import Referee
from serverRules import ServerRules

# Création de l'arbitre
referee = Referee(playerId='24052003',
						arena='survivalwaves',
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

# Reset de l'arène
referee.resetArena()

# Application des règles de l'arène
ServerRules(referee).applyRules()

# Lancement de l'arbitre
referee.run

noms_zombies = [
    "RigoloMort",
    "CervelleJoyeuse",
    "ZombiComique",
    "Risquatouille",
    "FarceurDécomposé",
]

import threading

instances = []

def create_zombie(name):
    instance = Zombie(name)
    instances.append(instance)
    instance.update()
    while True:
        instance.moveTowards(randint(0, 35), randint(0, 35))
        instance.update()
        sleep(1)
        print("Zombie", name, ":", instance.x, instance.y)
        
# Liste pour stocker les threads
threads = []

# Création de 10 threads, chacun appelant la fonction createZombie
for i in range(10):
    print("Création du thread", i)
    thread = threading.Thread(target=create_zombie, args=(noms_zombies[i],))
    threads.append(thread)
    thread.start()

# Attendre que tous les threads se terminent
for thread in threads:
    thread.join()

print("Tous les threads ont terminé.")

from dotenv import load_dotenv
import os
import j2l.pytactx.agent as pytactx
from time import sleep 
from random import randint
from Zombie import Zombie
import time
from Referee import Referee
from serverRules import ServerRules
from ZombieManager import ZombieManager

load_dotenv()
playerId = os.environ['PLAYER_ID']

# Création de l'arbitre
referee = Referee(playerId=playerId,
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

# Create zombies
zombie_manager = ZombieManager(arbitre, noms_zombies)
zombie_manager.create_zombies()

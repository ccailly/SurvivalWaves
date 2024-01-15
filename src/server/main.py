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
                        
referee.rulePlayer(referee.playerId, 'x', 0)
referee.rulePlayer(referee.playerId, 'y', 0)

# Reset de l'arène
referee.resetArena()

# Application des règles de l'arène
ServerRules(referee).applyRules()

# Lancement de l'arbitre
referee.run

# Création des zombies
zombies_names = [
    "RigoloMort",
    "CervelleJoyeuse",
    "ZombiComique",
    "Risquatouille",
    "FarceurDécomposé",
]
zombie_manager = ZombieManager(referee, zombies_names)
zombie_manager.create_zombies()
zombie_manager.run()

import j2l.pytactx.agent as pytactx
from time import sleep 
from random import randint
from Zombie import Zombie
import time
from Referee import Referee
from serverRules import ServerRules
from ZombieManager import ZombieManager

# Création de l'arbitre
referee = Referee(playerId='21122003',
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

# Zombies names
noms_zombies = [
    "RigoloMort",
    "CervelleJoyeuse",
    "ZombiComique",
    "Risquatouille",
    "FarceurDécomposé",
]

# Rules
arbitre.ruleArena("reset", True)
arbitre.ruleArena("profiles", ["arbitre", "zombie"])
arbitre.ruleArena("pIcons", ["👮", "🧟"])
arbitre.ruleArena("dtMove", [0, 1000])
arbitre.update()

# Create zombies
zombie_manager = ZombieManager(arbitre)
zombie_manager.create_zombies(noms_zombies)

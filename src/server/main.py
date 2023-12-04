import time
import j2l.pytactx.agent as pytactx
from serverRules import ServerRules

# Création de l'arbitre
arbitre = pytactx.Agent(playerId='24052003',
						arena='survivalwaves',
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

ServerRules(arbitre).applyRules()
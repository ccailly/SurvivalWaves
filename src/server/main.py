from dotenv import load_dotenv
import os
from Referee import Referee
from serverRules import ServerRules

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
referee.run()

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

# Définir le profile de l'arbitre
referee.rulePlayer(referee.playerId, 'profile', 2)

# Reset de l'arène
referee.resetArena()

# Application des règles de l'arène
ServerRules(referee).applyRules()

# Définir le profile de l'arbitre
referee.rulePlayer(referee.playerId, 'profile', 2)

# Lancement de l'arbitre
referee.run().join()
import j2l.pytactx.agent as pytactx
import time
import random

agent = pytactx.Agent(playerId="16052003",
						arena="survivalwaves",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

while True:
	agent.update()
	agent.moveTowards(random.randint(2,27),random.randint(2,27))
	
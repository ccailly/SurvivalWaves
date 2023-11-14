import j2l.pytactx.agent as pytactx
import time
import arme

agent = pytactx.Agent(playerId="helie",
						arena="survivalwaves",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

agent.moveTowards(2,2)
while True:
	agent.update()
	if (agent.x == 2 and agent.y == 2):
		print("droit")
		agent.moveTowards(27,2)
	if (agent.x == 27 and agent.y == 2):
		print("bas")
		agent.moveTowards(27,27)
	if (agent.x == 27 and agent.y == 27):
		print("gauche")
		agent.moveTowards(2,27)
	if (agent.x == 2 and agent.y == 27):
		print("haut")
		agent.moveTowards(2,2)


	print(str(agent.x) + " : " + str(agent.y))

	time.sleep(1)
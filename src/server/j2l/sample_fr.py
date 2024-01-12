import j2l.pytactx.agent as pytactx
from getpass import getpass

agent = pytactx.AgentFr(nom=input("👾 id: "),
                        arene=input("🎲 arena: "),
                        username="demo",
                        password=getpass("🔑 password: "),
                        url="mqtt.jusdeliens.com",
                        verbosite=3)

while True:
	agent.orienter((agent.orientation + 1) % 4)
	agent.actualiser()

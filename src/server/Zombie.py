import j2l.pytactx.agent as pytactx

class Zombie (pytactx.Agent):
    def __init__(self, name):
        super().__init__(
            playerId=name,
            arena="survivalwaves", 
            username="demo", 
            password="demo", 
            server="mqtt.jusdeliens.com", 
            verbosity=2) 
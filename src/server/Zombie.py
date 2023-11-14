import j2l.pytactx.agent as pytactx
from random import randint

class Zombie (pytactx.Agent):
    
    def __init__(self, name):
        super().__init__(
            playerId=name,
            arena="survivalwaves", 
            username="demo", 
            password="demo", 
            server="mqtt.jusdeliens.com", 
            verbosity=2
        )

    def wander(self):
        """
        Make the zombie wander randomly on the map
        """
        self.move(randint(-1, 1), randint(-1, 1))
        
    def chase(self, player):
        """
        Make the zombie chase a player
        """
        pass
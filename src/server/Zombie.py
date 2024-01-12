import j2l.pytactx.agent as pytactx
from random import randint

class Zombie (pytactx.Agent):

    def __init__(self, name: str) -> None:
        super().__init__(
            playerId=name,
            arena="survivalwaves", 
            username="demo", 
            password="demo", 
            server="mqtt.jusdeliens.com", 
            verbosity=2
        )

    def wander(self) -> None:
        """
        Make the zombie wander randomly on the map
        """
        self.move(randint(-1, 1), randint(-1, 1))

    def chase(self, x: int, y: int) -> None:
        """
        Make the zombie chase a player
        """
        self.moveTowards(x, y)

    def is_alive(self) -> bool:
        """
        Check if the zombie is alive
        """
        return self.life > 0

    def player_close(self) -> (int, int):
        """
        Check if a player is close to the zombie
        """
        for name, attributs in self.range.items():
            return (attributs['x'], attributs['y'])
        return None

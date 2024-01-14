from random import randint
from Referee import Referee

class Zombie:
    def __init__(self, referee: Referee, name: str) -> None:
        self.referee = referee
        self.name = name

    def wander(self) -> None:
        """
        Make the zombie wander randomly on the map
        """
        position = self.get_position()
        newX = position[0] + randint(-1, 1)
        newY = position[1] + randint(-1, 1)
        print(f"Zombie {self.name} wandering to {newX}, {newY}")
        self.referee.rulePlayer(self.name, 'x', newX)
        self.referee.rulePlayer(self.name, 'y', newY)
        self.referee.update()

    def chase(self) -> None:
        """
        Make the zombie chase a player
        """
        pass

    def get_position(self) -> tuple:
        """
        Get the zombie position
        """
        zombie = self.referee.range[self.name]
        return (zombie['x'], zombie['y'])

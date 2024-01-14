from Referee import Referee

class IZombie:
    def __init__(self, referee: Referee, name: str) -> None:
        """
        Initialize the zombie
        """
        pass

    def wander(self) -> None:
        """
        Make the zombie wander randomly on the map
        """
        pass
        
    def chase(self) -> None:
        """
        Make the zombie chase a player
        """
        pass

    def get_position(self) -> tuple:
        """
        Get the zombie's position
        """
        pass

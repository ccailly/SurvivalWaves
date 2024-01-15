from typing import Any
from states.IState import IState
from states.AbstractState import AbstractState

from ZombieManager import ZombieManager

class TickGameState(AbstractState):

    def __init__(self, referee, zombie_manager: ZombieManager):
        super().__init__(referee)
        self._zombie_manager = zombie_manager

    def process(self) -> None:
        pass

    def next(self) -> IState:
        """
        Returns the next state
        """
        return self
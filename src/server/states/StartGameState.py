from typing import Any
from states.IState import IState
from states.AbstractState import AbstractState
from states.TickGameState import TickGameState

from ZombieManager import ZombieManager

import threading

class StartGameState(AbstractState):
    def process(self) -> None:
        # Création des zombies
        zombies_names = [
            "RigoloMort",
            "CervelleJoyeuse",
            "ZombiComique",
            "Risquatouille",
            "FarceurDécomposé",
        ]
        self._zombie_manager = ZombieManager(self.getReferee(), zombies_names)
        self._zombie_manager.create_zombies()

        # Send the game started message to the players
        self._referee.ruleArena('info', 'Game started')

        # Reset the dxMax and dyMax to 1 to allow the players to move
        self._referee.ruleArena('dxMax', [1, 1, 1])
        self._referee.ruleArena('dyMax', [1, 1, 1])

        threading.Thread(target=self._zombie_manager.run).start()

    def next(self) -> IState:
        """
        Returns the next state
        """
        return TickGameState(self.getReferee(), self._zombie_manager)
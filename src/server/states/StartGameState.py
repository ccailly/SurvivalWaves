from typing import Any
from states.IState import IState
from states.AbstractState import AbstractState

class StartGameState(AbstractState):

    def process(self) -> None:
        self._referee.ruleArena('info', 'Game started')

        # Reset the dxMax and dyMax to 1 to allow the players to move
        self._referee.ruleArena('dxMax', [1, 1, 1])
        self._referee.ruleArena('dyMax', [1, 1, 1])

    def next(self) -> IState:
        """
        Returns the next state
        """
        return self
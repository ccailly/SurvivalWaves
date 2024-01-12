from states.IState import IState
from states.AbstractState import AbstractState
from states.StartGameState import StartGameState
import time

class WaitPlayersState(AbstractState):

    def checks(self) -> bool:
        """
        Checks if the game isn't running and if there 
        """
        return super().checks() and not self.getReferee().game_is_running() and len(self.getReferee().players) <= 1

    def process(self) -> None:
        if self.checks():
            self._referee.ruleArena('info', 'Waiting for players...')
        else:
            if not hasattr(self, "_timer"):
                self._timer = time.time()
            self._referee.ruleArena('info', 'Game is running in {}s'.format(max(0, round(30 - (time.time() - self._timer)))))

        # Check if the dxMax and dyMax are set to 0 to avoid the players to move
        self._referee.ruleArena('dxMax', [0, 1, 0])
        self._referee.ruleArena('dyMax', [0, 1, 0])

    def next(self) -> IState:
        """
        Returns the next state
        """
        return self if self.checks() or (hasattr(self, "_timer") and time.time() - self._timer < 30) else StartGameState(self.getReferee())
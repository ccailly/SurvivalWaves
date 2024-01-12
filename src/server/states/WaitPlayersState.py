from states.IState import IState
from states.AbstractState import AbstractState

class WaitPlayersState(AbstractState):

    def checks(self) -> bool:
        """
        Checks if the game isn't running and if there 
        """
        return super().checks() and not self.getReferee().game_is_running() and len(self.getReferee().players) <= 1

    def process(self) -> None:
        if self.checks():
            self._referee.ruleArena('info', 'Waiting for players...')

    def next(self) -> IState:
        """
        Returns the next state
        """
        return self
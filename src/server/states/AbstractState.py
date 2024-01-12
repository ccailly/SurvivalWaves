from states.IState import IState
from IReferee import IReferee

class AbstractState(IState):

    def __init__(self, referee: IReferee) -> None:
        super().__init__()
        self._referee = referee

    def checks(self) -> bool:
        return True

    def process(self) -> None:
        pass

    def getReferee(self) -> IReferee:
        return self._referee
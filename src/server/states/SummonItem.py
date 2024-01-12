from AbstractState import AbstractState

class SummonItemState(AbstractState):

    def checks(self) -> bool:
        return True

    def process(self) -> None:
        pass
class IState:

    def checks(self) -> bool:
        pass

    def process(self) -> None:
        pass

    def next(self) -> 'IState':
        pass
from states.abstract_state import *


class Dodgetate(AbstractState):
    def checks(self) -> bool:

        return super().checks()

    def process(self) -> None:
        if self.checks() == False:
            return

        super().process()

        closest_enemy = get_closest_enemy(self.agent)

        self.agent.moveTowards(closest_enemy[1]["x"], closest_enemy[1]["y"])
        self.agent.update()

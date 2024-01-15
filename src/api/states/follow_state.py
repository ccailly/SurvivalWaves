from states.abstract_state import *


class FollowState(AbstractState):
    def checks(self) -> bool:
        if not is_enemy_in_range(self.agent):
            self.instance.set_state("scan")
            return False

        if is_enemy_attackable(self.agent):
            self.instance.set_state("attack")
            return False

        return super().checks()

    def process(self) -> None:
        if self.checks() == False:
            return

        super().process()

        closest_enemy = get_closest_enemy(self.agent)

        self.agent.moveTowards(closest_enemy[1]["x"], closest_enemy[1]["y"])
        self.agent.update()

from states.abstract_state import *


class AttackState(AbstractState):
    def checks(self) -> bool:
        enemy = get_closest_enemy(self.agent)
        # if (
        #     enemy
        #     and enemy[1]["fire"]
        #     and [self.agent.x, self.agent.y] in enemy[1]["fire"]
        # ):
        #     print("Dodge")

        if not is_enemy_in_range(self.agent):
            self.instance.set_state("scan")
            return False

        if not is_enemy_attackable(self.agent):
            self.instance.set_state("follow")
            return False

        return super().checks()

    def process(self) -> None:
        if self.checks() == False:
            return

        super().process()

        closest_enemy = get_closest_enemy(self.agent)
        computed_dir = lookAtPosition(
            self.agent, closest_enemy[1]["x"], closest_enemy[1]["y"]
        )

        if self.agent.dir != computed_dir:
            self.agent.lookAt(computed_dir)
            self.agent.update()

        self.agent.fire(True)
        self.agent.update()

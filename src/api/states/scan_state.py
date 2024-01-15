from states.abstract_state import *
import random

class ScanState(AbstractState):


    def checks(self) -> bool:
        if is_enemy_in_range(self.agent):
            self.instance.set_state("follow")
            return False
        
        return super().checks()

    def process(self) -> None:
        if self.checks() == False:
            return 

        self.agent.moveTowards(
            random.randint(2, 33) , random.randint(2,34)
        )
        self.agent.update()

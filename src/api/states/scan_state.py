from states.abstract_state import *


class ScanState(AbstractState):


    def checks(self) -> bool:
        if is_enemy_in_range(self.agent):
            self.instance.set_state("follow")
            return False
        
        return super().checks()

    def process(self) -> None:
        if self.checks() == False:
            return
        point_TL = [9, 8]  
        point_TR = [25, 8]
        point_BR = [25, 25]
        point_BL = [9, 25]
        super().process()

        # Check if the agent is at the position
        # if (
        #     self.agent.x == self.instance.positions[0][0]
        #     and self.agent.y == self.instance.positions[0][1]
        # ):
        #     self.instance.positions.append(self.instance.positions.pop(0))
        #     return

        if self.agent.x == point_TL[0] and self.agent.y == point_TL[1]:
            self.agent.moveTowards(point_TR[0], point_TR[1])
        elif self.agent.x == point_TR[0] and self.agent.y == point_TR[1]:
            self.agent.moveTowards(point_BR[0], point_BR[1])
        elif self.agent.x == point_BR[0] and self.agent.y == point_BR[1]:
            self.agent.moveTowards(point_BL[0], point_BL[1])
        elif self.agent.x == point_BL[0] and self.agent.y == point_BL[1]:
            self.agent.moveTowards(point_TL[0], point_TL[1])    
        else :
            self.agent.moveTowards(point_TL[0], point_TL[1])

        self.agent.moveTowards(
            self.instance.positions[0][0], self.instance.positions[0][1]
        )
        self.agent.update()

import j2l.pytactx.agent as pytactx

from states.scan_state import ScanState
from states.follow_state import FollowState
from states.attack_state import AttackState

from utils import *


class Instance:
    def __init__(self, agent) -> None:
        self.agent = agent
        self.state = "scan"
        self.positions = generate_positions_to_scan()

    def loop(self) -> None:
        while True:
            # Check if the agent is firing
            if self.agent.isFiring and self.state != "attack":
                self.agent.fire(False)
                self.agent.update()

            match self.state:
                case "scan":
                    ScanState(self).process()
                case "follow":
                    FollowState(self).process()
                case "attack":
                    AttackState(self).process()

    def get_agent(self) -> pytactx.Agent:
        return self.agent

    def get_state(self) -> str:
        return self.state

    def set_state(self, state: str) -> None:
        self.state = state

    def get_positions(self) -> list:
        return self.positions


if __name__ == "__main__":
    agent = pytactx.Agent(
        playerId="Helie",
        arena="survivalwaves",
        username="demo",
        password="demo",
        server="mqtt.jusdeliens.com",
        verbosity=2,
    )

    instance = Instance(agent)
    instance.loop()

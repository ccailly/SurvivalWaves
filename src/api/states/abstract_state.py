import math


class AbstractState(object):
    def __init__(self, instance) -> None:
        self.instance = instance
        self.agent = instance.agent

    def checks(self) -> bool:
        return True

    def process(self) -> None:
        pass


# Check if an enemy is in range
def is_enemy_in_range(agent) -> bool:
    for name, attribut in agent.range.items() :
        if attribut['profile'] == 2 :
            return True
    return False

# Check if an enemy is attackable
def is_enemy_attackable(agent):
    if is_enemy_in_range(agent):
        closest_enemy = get_closest_enemy(agent)
        if (
            math.sqrt(
                (agent.x - closest_enemy[1]["x"]) ** 2
                + (agent.y - closest_enemy[1]["y"]) ** 2
            )
            <= 8
        ):
            return True

    return False


# Get the closest enemy
def get_closest_enemy(agent):
    closest_enemy = None
    closest_distance = math.inf
    for enemy in agent.range.items():
        distance = math.sqrt(
            (agent.x - enemy[1]["x"]) ** 2 + (agent.y - enemy[1]["y"]) ** 2
        )
        if distance < closest_distance and enemy[1]["profile"] == 2:
            closest_enemy = enemy
            closest_distance = distance
    return closest_enemy


# Look at a position
def lookAtPosition(agent, x, y):
    if x - agent.x < 0:
        return 2
    elif x - agent.x > 0:
        return 0
    elif y - agent.y < 0:
        return 1
    elif y - agent.y > 0:
        return 3
    else:
        return agent.dir

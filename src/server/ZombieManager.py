from Zombie import Zombie
from time import sleep

class ZombieManager:
    def __init__(self, referee, zombies_names: list):
        self.zombies = []
        self.referee = referee
        self.zombies_names = zombies_names

    def create_zombies(self):
        """
        Create zombies in the arena
        """
        for name in self.zombies_names:
            self.zombies.append(Zombie(self.referee, name))
            self.referee.rulePlayer(name, 'profile', 2)
            self.referee.rulePlayer(name, 'team', 1)
            self.referee.rulePlayer(name, 'life', 50)
            self.referee.rulePlayer(name, 'x', 14)
            self.referee.rulePlayer(name, 'y', 6)
        self.referee.update()    
        sleep(0.3)

    def remove_zombies(self):
        """
        Remove all zombies from the arena
        """
        self.zombies = []
        for name, attributs in self.referee.range.items():
            self.referee.rulePlayer(name, 'life', 0)
        self.referee.update()    
        sleep(0.3)

    def zombies_action(self):
        """
        Make all zombies do an action
        """
        zombies_alive = self.referee.range
        for zombie in self.zombies:
            if zombie.name in zombies_alive:
                self.action(zombie)
            else:
                # self.zombies.remove(zombie)

    def action(self, zombie: Zombie) -> None:
        """
        Make a zombie do an action
        """
        zombie.wander()

    def run(self):
        """
        Run the zombie manager
        """
        while True:
            self.zombies_action()
            sleep(0.5)

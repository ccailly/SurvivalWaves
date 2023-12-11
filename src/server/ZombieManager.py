from Zombie import Zombie
import threading
import j2l.pytactx.agent as pytactx
from time import sleep

class ZombieManager:
    
    def __init__(self, arbitre: pytactx.Agent, zombies_names: list):
        self.zombies = []
        self.arbitre = arbitre
        self.zombies_names = zombies_names

    def create_zombie(self, name: str):
        """
        Generate a zombie instance
        """
        zombie = Zombie(name)
        zombie.update()
        
        self.zombie_rules(name)
        self.manage_state(zombie)

    def create_zombies(self):
        """
        Generate a list of zombies instances from a list of names
        """
        
        # Create a thread for each zombie
        for name in self.zombies_names:
            print("Création du thread", name)
            thread = threading.Thread(target=self.create_zombie, args=(name,))
            self.zombies.append(thread)
            thread.start()
            
        # Wait for all threads to finish
        for thread in self.zombies:
            thread.join()
            
        print("Tous les threads ont terminé.")

    def zombie_rules(self, name: str):
        """
        Define the rules for the zombies
        """
        # Change the profile of the zombie
        self.arbitre.rulePlayer(name, 'profile', 1)
        self.arbitre.update()

    def manage_state(self, zombie: Zombie):
        """
        Manage the state (wander or chase) of the zombies
        """
        while True:
            if not zombie.is_alive():
                print("Le zombie", zombie.playerId, "est mort.")
                break
            
            zombie.wander()
            zombie.update()

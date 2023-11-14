from Zombie import Zombie
import threading

class ZombieManager:
    
    def __init__(self, arbitre):
        self.zombies = []

    def create_zombie(self, name: str):
        """
        Generate a zombie instance
        """
        zombie = Zombie(name)
        
        while True:
            zombie.wander()
            
            # TODO: Add here the behavior of the zombie
            
            zombie.update()

    def create_zombies(self, zombies_names: list):
        """
        Generate a list of zombies instances from a list of names
        """
        
        # Create a thread for each zombie
        for name in zombies_names:
            print("Création du thread", name)
            thread = threading.Thread(target=self.create_zombie, args=(name,))
            self.zombies.append(thread)
            thread.start()
            
        # Wait for all threads to finish
        for thread in self.zombies:
            thread.join()
            
        print("Tous les threads ont terminé.")

import IReferee
import threading
import time
from states.WaitPlayersState import WaitPlayersState

class Referee(IReferee.IReferee):

    def __init__(self, playerId: str = None, arena: str = None, username: str = None, password: str = None, server: str = None, port: int = 1883, imgOutputPath: str = "img.jpeg", autoconnect: bool = True, waitArenaConnection: bool = True, verbosity: int = 3, robotId: str = "_", welcomePrint: bool = True, sourcesdir: str = None):
        super().__init__(playerId, arena, username, password, server, port, imgOutputPath, autoconnect, waitArenaConnection, verbosity, robotId, welcomePrint, sourcesdir)
        self._thread = None
        self._game_is_running = False
        self._state = WaitPlayersState(self)

    def get_thread(self) -> threading.Thread:
        return self._thread
    
    def game_is_running(self) -> bool:
        return self._game_is_running
    
    def resetArena(self) -> None:
        self.ruleArena("reset", True)
        self.update()
        time.sleep(3)

    def run(self):
        self._thread = threading.Thread(target=self._thread_run)
        self._thread.start()
        return self._thread

    def _thread_run(self):
        while True:
            self._state.process()
            self._state = self._state.next()

            self.update()
            time.sleep(0.1)

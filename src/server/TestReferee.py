import unittest
from unittest.mock import MagicMock
import threading
import time
from states.WaitPlayersState import WaitPlayersState
from Referee import Referee

class TestReferee(unittest.TestCase):
    def setUp(self):
        self.referee = Referee()
        self.mock_state = MagicMock(spec=WaitPlayersState)
        self.referee._state = self.mock_state

    def test_game_is_running(self):
        self.assertFalse(self.referee.game_is_running())

    def test_resetArena(self):
        self.referee.ruleArena = MagicMock()
        self.referee.update = MagicMock()

        self.referee.resetArena()

        # Asserts: check that ruleArena and update methods are called
        self.referee.ruleArena.assert_called_once_with("reset", True)
        self.referee.update.assert_called_once()

    def test_run(self):
        self.referee._thread_run = MagicMock()

        thread = self.referee.run()

        # Asserts: check that _thread_run method is called and that the returned value is a thread
        self.referee._thread_run.assert_called_once()
        self.assertIsInstance(thread, threading.Thread)

if __name__ == '__main__':
    unittest.main()

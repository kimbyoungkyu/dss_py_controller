from abc import ABC, abstractmethod
from core.state import DSSState
from core.control import ControlCommand

class DSSController(ABC):
    def on_init(self):
        print("[Controller] init")

    @abstractmethod
    def on_update(self, state: DSSState) -> ControlCommand:
        pass

    def on_shutdown(self):
        print("[Controller] shutdown")

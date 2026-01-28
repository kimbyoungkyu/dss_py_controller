from dataclasses import dataclass

@dataclass
class ControlCommand:
    throttle: float = 0.0
    brake: float = 0.0
    steer: float = 0.0
    targetGear: int = 1

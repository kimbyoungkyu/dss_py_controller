from core.controller_base import DSSController
from core.control import ControlCommand

class RuleController(DSSController):
    def on_update(self, state):
        if state.camera:
            print(f"[RuleController] camera frame {state.camera.width}x{state.camera.height}")
            
            
            
            
        return ControlCommand(
            throttle=1.3,
            steer=-state.vehicle.yaw * 0.5
        )

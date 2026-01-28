import math, time
from core.state import DSSState, VehicleState, IMUState, CameraState

class FakeSensor:
    def __init__(self):
        self.t = 0.0
        print("[FakeSensor] started")

    def get_state(self):
        time.sleep(0.05)
        self.t += 0.05
        return DSSState(
            vehicle=VehicleState(self.t, math.sin(self.t), math.sin(self.t)*0.3),
            imu=IMUState(0,0,0,0,0,0),
            camera=CameraState(
                width=640,
                height=480,
                encoding="fake",
                data=b""
            )
        )

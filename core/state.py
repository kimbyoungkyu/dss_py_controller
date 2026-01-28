from dataclasses import dataclass
from typing import Optional

@dataclass
class VehicleState:
    x: float
    y: float
    yaw: float

@dataclass
class IMUState:
    ax: float
    ay: float
    az: float
    wx: float
    wy: float
    wz: float

@dataclass
class CameraState:
    width: int
    height: int
    encoding: str
    data: bytes        # raw or compressed image bytes

@dataclass
class DSSState:
    vehicle: VehicleState
    imu: IMUState
    camera: Optional[CameraState] = None
    speed: float = 0.0

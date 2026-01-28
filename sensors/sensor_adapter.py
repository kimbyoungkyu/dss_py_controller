import asyncio, threading, numpy as np
from nats.aio.client import Client as NATS
from proto import dss_pb2
from core.state import DSSState, VehicleState, IMUState, CameraState

class SensorAdapter:
    def __init__(self, nats_url="nats://127.0.0.1:4222"):
        print("[SensorAdapter] init")
        self.nats_url = nats_url
        self.latest_state = None

        self.vehicle = None
        self.imu = None
        self.camera = None

        self.nc = NATS()
        self.loop = asyncio.new_event_loop()
        threading.Thread(target=self._run, daemon=True).start()

    def _run(self):
        print("[SensorAdapter] event loop start")
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self._connect())
        self.loop.run_forever()

    async def _connect(self):
        print("[SensorAdapter] connecting to NATS:", self.nats_url)
        await self.nc.connect(self.nats_url)
        print("[SensorAdapter] connected")

        await self.nc.subscribe("dss.odom", cb=self._odom_cb)
        await self.nc.subscribe("dss.sensor.imu", cb=self._imu_cb)
        await self.nc.subscribe("dss.sensor.camera.rgb", cb=self._camera_cb)

        print("[SensorAdapter] subscribed odom / imu / camera")

    def _quat_to_yaw(self, q):
        return np.arctan2(
            2*(q.w*q.z + q.x*q.y),
            1 - 2*(q.y*q.y + q.z*q.z)
        )

    async def _odom_cb(self, msg):
        od = dss_pb2.DSSOdom()
        od.ParseFromString(msg.data)
        self.vehicle = VehicleState(
            x=od.pose.position.x,
            y=od.pose.position.y,
            yaw=self._quat_to_yaw(od.pose.orientation)
        )
        #print("[SensorAdapter] odom received")
        self._update()

    async def _imu_cb(self, msg):
        imu = dss_pb2.DSSIMU()
        imu.ParseFromString(msg.data)
        self.imu = IMUState(
            ax=imu.linear_acceleration.x,
            ay=imu.linear_acceleration.y,
            az=imu.linear_acceleration.z,
            wx=imu.angular_velocity.x,
            wy=imu.angular_velocity.y,
            wz=imu.angular_velocity.z
        )
        #print("[SensorAdapter] imu received")
        self._update()

    async def _camera_cb(self, msg):
        img = dss_pb2.DSSImage()
        img.ParseFromString(msg.data)
        self.camera = CameraState(
            width=img.width,
            height=img.height,
            encoding=img.encoding,
            data=img.data
        )
        print(f"[SensorAdapter] camera received {img.width}x{img.height} {img.encoding}")
        self._update()

    def _update(self):
        if self.vehicle and self.imu:
            self.latest_state = DSSState(
                vehicle=self.vehicle,
                imu=self.imu,
                camera=self.camera
            )
            #print("[SensorAdapter] state updated")

    def get_state(self):
        return self.latest_state

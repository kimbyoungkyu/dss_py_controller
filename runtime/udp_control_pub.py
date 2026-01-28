import socket, time
from proto import dss_pb2

class UDPControlPublisher:
    def __init__(self, ip="127.0.0.1", port=8886):
        self.addr = (ip, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(f"[UDP Publisher] target {ip}:{port}")

    def publish(self, cmd):
        msg = dss_pb2.DssSetControl(
            throttle=cmd.throttle,
            brake=cmd.brake,
            steer=cmd.steer,
            targetGear=cmd.targetGear,
            timestamp=int(time.time()*1000)
        )
        self.sock.sendto(msg.SerializeToString(), self.addr)
        print("[UDP Publisher] sent:", cmd)

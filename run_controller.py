import argparse
from controllers.rule_controller import RuleController
from runtime.controller_runtime import ControllerRuntime
from runtime.udp_control_pub import UDPControlPublisher
from sensors.sensor_adapter import SensorAdapter
from sensors.fake_sensor import FakeSensor

parser = argparse.ArgumentParser()
parser.add_argument("--fake", action="store_true")
parser.add_argument("--udp-ip", default="127.0.0.1")
parser.add_argument("--udp-port", type=int, default=8886)
args = parser.parse_args()

print("[Main] start")

controller = RuleController()
sensor = FakeSensor() if args.fake else SensorAdapter()
publisher = UDPControlPublisher(args.udp_ip, args.udp_port)

ControllerRuntime(controller, sensor, publisher).run()

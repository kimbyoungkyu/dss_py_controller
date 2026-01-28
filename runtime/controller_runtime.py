import time

class ControllerRuntime:
    def __init__(self, controller, sensor, publisher, hz=50):
        print("[Runtime] init")
        self.controller = controller
        self.sensor = sensor
        self.publisher = publisher
        self.dt = 1.0 / hz

    def run(self):
        print("[Runtime] run loop start")
        self.controller.on_init()
        while True:
            state = self.sensor.get_state()
            if state:
                cmd = self.controller.on_update(state)
                self.publisher.publish(cmd)
            else:
                print("[Runtime] waiting for state...")
            time.sleep(self.dt)

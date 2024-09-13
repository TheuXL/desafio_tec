from controller import SwitchController

def simulate_lights():
    controller = SwitchController()
    lights_status = controller.simulate()
    for switch, status in lights_status.items():
        print(f"Interruptor {switch}: Status - {status['status']}, Temperatura - {status['temperature']}")

if __name__ == "__main__":
    simulate_lights()

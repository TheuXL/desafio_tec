import time

class SwitchController:
    def __init__(self):
        self.lights = {
            'A': {'status': 'desligado', 'temperature': 'fria'},
            'B': {'status': 'desligado', 'temperature': 'fria'},
            'C': {'status': 'desligado', 'temperature': 'fria'}
        }

    def turn_on(self, switch_id):
        if switch_id in self.lights:
            self.lights[switch_id]['status'] = 'ligado'
            self.lights[switch_id]['temperature'] = 'quente'
            print(f"Interruptor {switch_id} ligado")

    def turn_off(self, switch_id):
        if switch_id in self.lights:
            self.lights[switch_id]['status'] = 'desligado'
            if self.lights[switch_id]['temperature'] == 'quente':
                self.lights[switch_id]['temperature'] = 'morno'
            print(f"Interruptor {switch_id} desligado")

    def get_light_status(self, switch_id):
        return self.lights.get(switch_id, None)

    def simulate(self):
        # Passo 1: Ligue o interruptor A
        self.turn_on('A')
        time.sleep(10)  # Espera por 10 minutos em um cenário real

        # Passo 2: Desligue o interruptor A e ligue o interruptor B
        self.turn_off('A')
        self.turn_on('B')

        # Passo 3: Verifique o status das lâmpadas
        return self.lights

import unittest
from controller import SwitchController

class TestSwitchController(unittest.TestCase):
    def test_switch_controller(self):
        controller = SwitchController()
        controller.turn_on('A')
        controller.turn_off('A')
        controller.turn_on('B')
        lights = controller.simulate()
        
        self.assertEqual(lights['A']['status'], 'desligado')
        self.assertEqual(lights['A']['temperature'], 'morno')
        self.assertEqual(lights['B']['status'], 'ligado')
        self.assertEqual(lights['B']['temperature'], 'quente')
        self.assertEqual(lights['C']['status'], 'desligado')
        self.assertEqual(lights['C']['temperature'], 'fria')

if __name__ == '__main__':
    unittest.main()

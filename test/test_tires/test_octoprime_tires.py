import unittest

from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tires_array = [0.5, 1, 1, 0.5]
        tires = OctoprimeTires(tires_array)
        self.assertTrue(tires)

    def test_needs_service_false(self):
        tires_array = [0.5, 1, 0.49, 1]
        tires = OctoprimeTires(tires_array)
        self.assertFalse(tires)
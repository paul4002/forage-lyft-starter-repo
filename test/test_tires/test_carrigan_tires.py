import unittest

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tires_array = [0, 0, 0.9, 0]
        tires = CarriganTires(tires_array)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires_array = [0.5, 0, 0.89, 0]
        tires = CarriganTires(tires_array)
        self.assertFalse(tires.needs_service())
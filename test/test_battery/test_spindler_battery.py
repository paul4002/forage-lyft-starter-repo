import unittest

from datetime import datetime

from battery.spindler_battery import SpindlerBattery
from utils.date_utils import substract_years_to_date

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.today().date()
        last_service_date = substract_years_to_date(current_date, 4)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = substract_years_to_date(current_date, 2)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
import unittest

from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from utils.date_utils import substract_years_to_date

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.today().date()
        last_service_date = substract_years_to_date(current_date, 5)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = substract_years_to_date(current_date, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
#!/usr/bin/env python3
from dateutil.relativedelta import relativedelta
from datetime import datetime
from pytz import timezone
from src import timekit
import unittest

# Updating the test cases to use the adjusted function

class TestConfigureTimeAdjusted(unittest.TestCase):
    def test_default_settings(self):
        # Testing with default settings
        result = timekit.configure_time()
        self.assertIsNotNone(result)

    def test_time_zone_conversion(self):
        # Testing with a different timezone
        result = timekit.configure_time(time_zone="America/New_York")
        self.assertIsNotNone(result)

    def test_format_change(self):
        # Testing with a different format
        result = timekit.configure_time(format="%Y-%m-%d %H:%M:%S")
        self.assertIsNotNone(result)

    def test_date_manipulation_replace(self):
        # Testing date manipulation with replace method
        result = timekit.configure_time(year=2020, month=12, day=25)
        self.assertIn("25-12-2020", result)

    def test_relative_delta_addition(self):
        # Testing date manipulation with relative delta addition
        current_date = datetime.now().astimezone(timezone("Europe/Tallinn"))
        future_date = current_date + relativedelta(days=10, months=1)
        result = timekit.configure_time(delta={"days": 10, "months": 1})
        expected_date = future_date.strftime("%d-%m-%YT%H:%M")
        self.assertEqual(result, expected_date)

    def test_relative_delta_subtraction(self):
        # Testing relative delta subtraction for the last day of the previous month
        current_date = datetime.now().astimezone(timezone("Europe/Tallinn"))
        last_day_prev_month = current_date + relativedelta(months=-1, days=31)
        result = timekit.configure_time(delta={"months": -1, "days": 31})
        expected_date = last_day_prev_month.strftime("%d-%m-%YT%H:%M")
        self.assertEqual(result, expected_date)

    def test_combine_replace_and_delta(self):
        # Testing combination of replace and delta with time components
        result = timekit.configure_time(year=2021, month=1, day=15, hour=0, minute=0, second=0, delta={"weeks": -2})
        expected_date = (datetime(2021, 1, 15, 0, 0, 0) + relativedelta(weeks=-2)).strftime("%d-%m-%YT%H:%M")
        self.assertEqual(result, expected_date)

# Running the updated tests
unittest.main(argv=[''], exit=False)

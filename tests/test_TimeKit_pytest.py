#!/usr/bin/env python3
import pytest
from dateutil.relativedelta import relativedelta
from datetime import datetime
from pytz import timezone
from src.timekit import configure_time  # replace 'your_module' with the actual module name

# Test default settings
def test_default_settings():
    result = configure_time()
    assert result is not None

# Test time zone conversion
def test_time_zone_conversion():
    result = configure_time(time_zone="America/New_York")
    assert result is not None

# Test format change
def test_format_change():
    result = configure_time(format="%Y-%m-%d %H:%M:%S")
    assert result is not None

# Test date manipulation (replace method)
def test_date_manipulation_replace():
    result = configure_time(year=2020, month=12, day=25)
    assert "25-12-2020" in result

# Test relative delta addition
def test_relative_delta_addition():
    current_date = datetime.now().astimezone(timezone("Europe/Tallinn"))
    future_date = current_date + relativedelta(days=10, months=1)
    result = configure_time(delta={"days": 10, "months": 1})
    expected_date = future_date.strftime("%d-%m-%YT%H:%M")
    assert result == expected_date

# Test relative delta subtraction
def test_relative_delta_subtraction():
    current_date = datetime.now().astimezone(timezone("Europe/Tallinn"))
    last_day_prev_month = current_date + relativedelta(months=-1, days=31)
    result = configure_time(delta={"months": -1, "days": 31})
    expected_date = last_day_prev_month.strftime("%d-%m-%YT%H:%M")
    assert result == expected_date

# Test combination of replace and delta
def test_combine_replace_and_delta():
    result = configure_time(year=2021, month=1, day=15, hour=0, minute=0, second=0, delta={"weeks": -2})
    expected_date = (datetime(2021, 1, 15, 0, 0, 0) + relativedelta(weeks=-2)).strftime("%d-%m-%YT%H:%M")
    assert result == expected_date

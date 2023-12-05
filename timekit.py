#!/usr/bin/env python3
# @Author: Tanel Treuberg
# @Github: https://github.com/The-Magicians-Code
# @Description: Configure datetime object based on the given keyword arguments.

from dateutil.relativedelta import relativedelta
from datetime import datetime
from pytz import timezone

def configure_time(time_zone: str="Europe/Tallinn", format: str="%d-%m-%YT%H:%M", **kwargs: dict) -> str:
    """
    Configure datetime object based on the given keyword arguments.

    :param time_zone: (str) Timezone to use (default "Europe/Tallinn").
    :param format: (str) Format to use (default "%d-%m-%YT%H:%M").
    :param kwargs: (dict) Keyword arguments to manipulate the datetime object.

    :return: (str) Datetime object as a string.

    Example:
    # Get the last day of the previous month in Europe/London timezone
    configure_time(time_zone="Europe/London", format="%d-%m-%YT%H:%M %z", day=1, delta={"days": -1})
    
    # Also another method of solving the first problem by using the "month" keyword argument and setting the days to 31
    # which will automatically determine the last day of the previous month and is the maximum amount of days in a month
    configure_time(time_zone="Europe/London", format="%d-%m-%YT%H:%M %z", delta={"months": -1, "days": 31})

    This function configures a datetime object based on the provided time_zone and format.
    It allows manipulation of the datetime object using valid keyword arguments for datetime.replace().
    Additionally, you can use the "delta" keyword argument to subtract time intervals using datetime.timedelta().

    For valid keyword arguments and their descriptions, refer to the official Python documentation:
    https://docs.python.org/3/library/datetime.html#datetime.datetime.replace
    https://dateutil.readthedocs.io/en/stable/relativedelta.html
    """

    # Get current datetime object and configure it's timezone
    result = datetime.now().astimezone(timezone(time_zone))

    # Only use the keyword arguments that are valid for the datetime.replace() method
    # https://docs.python.org/3/library/datetime.html#datetime.datetime.replace
    attributes = {key: value for key, value in kwargs.items() if key in ["year", "month", "day", "hour", "minute", "second"]}
    result = result.replace(**attributes)
    
    # Use the relativedelta() to manipulate the datetime object to get the last month or last week etc
    if "delta" in kwargs:
        result += relativedelta(**kwargs["delta"])

    # Format datetime object based on the given format
    result = result.strftime(format)

    return result
    
# Test cases
if __name__ == "__main__":
    # Feed in a dictionary of keyword arguments
    conf = {
        "yesterday_day": {
            "format": "%Y-%m-%d",
            "delta": {"days": -1}
        }
    }
    print(configure_time(**conf["yesterday_day"]))

# TimeKit
Simplified datetime object manipulator

### Install
````
pip3 install -r requirements.txt
````

### Test Cases
````python3
import timekit

# Get current datetime object in Europe/Tallinn timezone
print(timekit.configure_time(time_zone="Europe/Tallinn"))

# Get datetime object for 1st of January 2022 in Europe/Tallinn timezone
print(timekit.configure_time(time_zone="Europe/Tallinn", month=1, day=1))

# Get datetime object for 1st of January 2022 at 12:00 in Europe/Tallinn timezone
print(timekit.configure_time(time_zone="Europe/Tallinn", year=2022, month=2, day=3, hour=12, minute=5))

# Get datetime object for 1st of January 2022 at 12:00 in UTC timezone
print(timekit.configure_time(time_zone="UTC", year=1992, month=5, day=8, hour=11, minute=0))

# Format datetime object as "YYYY-MM-DD HH:MM"
print(timekit.configure_time(time_zone="Europe/Tallinn", format="%Y-%m-%d %H:%M %z"))

# Get datetime object for today in Europe/Tallinn timezone and subtract 1 month
print(timekit.configure_time(time_zone="Europe/Tallinn", delta={"months": -1}))

# Get datetime object for the last day of the previous month in Europe/Tallinn timezone
print(timekit.configure_time(time_zone="Europe/Tallinn", day=1, delta={"days": -1}))
````

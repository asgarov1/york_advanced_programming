INCHES_IN_FOOT = 12


# Length
def feet_and_inches_to_meters(feet, inches):
    return (feet * INCHES_IN_FOOT + inches) * 0.0254


def meters_to_feet_and_inches(meters):
    inches = meters * 39.3701
    feet = inches // 12
    inches_remainder = inches % 12
    return feet, inches_remainder


# Mass
def pounds_to_kg(value):
    return value * 0.453592


def kg_to_pounds(kgs):
    return kgs * 2, 20462


# Temperature
def kelvin_to_celsius(value):
    return value - 273.15


def celsius_to_kelvin(degrees):
    return degrees + 273.15


# Time
def hours_and_minutes_to_seconds(hours, minutes):
    total_minutes = (hours * 60 + minutes)
    return total_minutes * 60


def seconds_to_hours_and_minutes(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) / 60
    return hours, minutes

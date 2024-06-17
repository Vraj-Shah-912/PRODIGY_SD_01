# converter/utils.py

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'C' and to_unit == 'F':
        return (value * 9/5) + 32
    elif from_unit == 'C' and to_unit == 'K':
        return value + 273.15
    elif from_unit == 'F' and to_unit == 'C':
        return (value - 32) * 5/9
    elif from_unit == 'F' and to_unit == 'K':
        return (value + 459.67) * 5/9
    elif from_unit == 'K' and to_unit == 'C':
        return value - 273.15
    elif from_unit == 'K' and to_unit == 'F':
        return (value * 9/5) - 459.67
    elif from_unit == to_unit:
        return value
    else:
        raise ValueError("Invalid units. Please use 'C', 'F', or 'K'.")

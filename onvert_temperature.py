
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            print (f"{((value *1.8)+32):.4f}")
        elif to_unit == 'kelvin':
            print (f"{(value + 273.15):.4f}")
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            print (f"{((value - 32) * 1.8):.4f}")
        elif to_unit == 'kelvin':
            print (f"{((value - 32) * 1.8 + 273.15):.4f}")
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            print (f"{(value - 273.15):.4f}")
        elif to_unit == 'fahrenheit':
            print (f"{((value - 273.15) * 1.8 + 32):.4f}")
convert_temperature(float(input()), input(),input())

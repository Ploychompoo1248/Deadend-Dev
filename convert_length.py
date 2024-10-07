"""convert_length"""
def meters(value, to_unit):
    """convert meters to others"""
    if to_unit == "feet":
        print(f"{value*3.28084:.4f}")
    elif to_unit == "inches":
        print(f"{value * 39.3701:.4f}")
    elif to_unit == "miles":
        print(f"{value/1609.34708789:.4f}")
    elif to_unit == "kilometers":
        print(f"{value/1000:.4f}")

def kilometers(value, to_unit):
    """convert kilometers to others"""
    if to_unit == "inches":
        print(f"{value*39370.1:.4f}")
    elif to_unit == "meters":
        print(f"{value * 1000:.4f}")
    elif to_unit == "miles":
        print(f"{value/1.6093445:.4f}")
    elif to_unit == "feet":
        print(f"{value * 3280.84:.4f}")

def miles(value, to_unit):
    """convert miles to others"""
    if to_unit == "inches":
        print(f"{value*63360:.4f}")
    elif to_unit == "meters":
        print(f"{value * 1609.34449789:.4f}")
    elif to_unit == "kilometers":
        print(f"{value * 1.6093445:.4f}")
    elif to_unit == "feet":
        print(f"{value * 5280:.4f}")

def feet(value, to_unit):
    """convert feet to others"""
    if to_unit == "inches":
        print(f"{value*12:.4f}")
    elif to_unit == "meters":
        print(f"{value * 0.3048:.4f}")
    elif to_unit == "miles":
        print(f"{value/5280:.4f}")
    elif to_unit == "kilometers":
        print(f"{value/3280.83989501:.4f}")

def inches(value,to_unit):
    """convert inches to others"""
    if to_unit == "feet":
        print(f"{value/12:.4f}")
    elif to_unit == "meters":
        print(f"{value/39.37009424:.4f}")
    elif to_unit == "miles":
        print(f"{value/63360:.4f}")
    elif to_unit == "kilometers":
        print(f"{value/39370.07874016:.4f}")

def main(value, from_unit, to_unit):
    if from_unit == "meters":
        meters(value,to_unit)
    elif from_unit == "kilometers":
        kilometers(value,to_unit)
    elif from_unit == "miles":
        miles(value,to_unit)
    elif from_unit == "feet":
        feet(value,to_unit)
    elif from_unit == "inches":
        inches(value,to_unit)
    elif from_unit == to_unit :
        print(value)
    elif value == "0":
        print("0.0000")
main(float(input()),input(),input())

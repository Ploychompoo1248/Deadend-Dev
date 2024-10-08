"""convert_weight"""
def grams(value, to_unit):
    """convert grams to others"""
    if to_unit == "kilograms":
        print(f"{value/1000:.4f}")
    elif to_unit == "pounds":
        print(f"{value / 453.59290944:.4f}")
    elif to_unit == "ounces":
        print(f"{value / 28.34949254:.4f}")

def kilograms(value, to_unit):
    """convert kilograms to others"""
    if to_unit == "grams":
        print(f"{value*1000:.4f}")
    elif to_unit == "pounds":
        print(f"{value * 2.20462:.4f}")
    elif to_unit == "ounces":
        print(f"{value * 35.274:.4f}")

def pounds(value, to_unit):
    """convert pounds to others"""
    if to_unit == "grams":
        print(f"{value*453.59290944:.4f}")
    elif to_unit == "kilograms":
        print(f"{value / 2.20462:.4f}")
    elif to_unit == "ounces":
        print(f"{value * 16:.4f}")

def ounces(value, to_unit):
    """convert ounces to others"""
    if to_unit == "grams":
        print(f"{value*28.34949254:.4f}")
    elif to_unit == "kilograms":
        print(f"{value / 35.274:.4f}")
    elif to_unit == "pounds":
        print(f"{value / 16:.4f}")

def main(value, from_unit, to_unit):
    """process"""
    if from_unit == "grams":
        grams(value,to_unit)
    elif from_unit == "kilograms":
        kilograms(value,to_unit)
    elif from_unit == "pounds":
        pounds(value,to_unit)
    elif from_unit == "ounces":
        ounces(value,to_unit)
    elif from_unit == to_unit :
        print(value)
    elif value == "0":
        print("0.0000")
main(float(input()),input(),input())

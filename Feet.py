"""Feet"""
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
    elif value == "0":
        print("0.0000")
feet(float(input()),input())

"""Meters"""
def meter(value, to_unit):
    """convert meters to others"""
    if to_unit == "feet":
        print(f"{value*3.28084:.4f}")
    elif to_unit == "inches":
        print(f"{value * 39.3701:.4f}")
    elif to_unit == "miles":
        print(f"{value/1609.34708789:.4f}")
    elif to_unit == "kilometers":
        print(f"{value/1000:.4f}")
    elif value == "0":
        print("0.0000")
meter(float(input()),input())

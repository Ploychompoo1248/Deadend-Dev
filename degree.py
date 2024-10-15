"""degree"""
def main(value, from_unit, to_unit):
    """process"""
    if from_unit == "degrees" and to_unit == "radians":
            print(f"{(value*(3.14159/180)):.4f}")
    elif from_unit == "radians" and to_unit == "degrees":
        print(f"{((value*180)/3.14159):.4f}")
    elif from_unit == to_unit :
        print(value)
    elif value == "0":
        print("0.0000")
main(float(input()),input(),input())

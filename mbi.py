"""bmi"""
def main():
    """process"""
    weight = float(input()) #kg
    height = (float(input())/100) #cm
    bmi = (weight / (height * height))
    print(f"{bmi:.2f}")
    if bmi < 18.50:
        print("น้ำหนักน้อย / ผอม")
    elif 18.50 <= bmi <= 22.99:
        print("ปกติ (สุขภาพดี)")
    elif 23 <= bmi <= 24.99:
        print("ท้วม / อ้วนระดับที่ 1")
    elif 25 <= bmi <= 29.99:
        print("อ้วน / อ้วนระดับที่ 2")
    elif 30 <= bmi:
        print("อ้วนมาก / อ้วนระดับที่ 3")
main()

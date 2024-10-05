def convert_length(value, from_unit, to_unit): # แปลงความยาว
    units = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'miles': 1609.34,
        'feet': 0.3048,
        'inches': 0.0254
    }
    return value * (units[to_unit] / units[from_unit])

def convert_weight(value, from_unit, to_unit): # แปลงน้ำหนัก มวล
    units = {
        'grams': 1.0,
        'kilograms': 1000.0,
        'pounds': 453.592,
        'ounces': 28.3495
    }
    return value * (units[to_unit] / units[from_unit])

def convert_temperature(value, from_unit, to_unit): # แปลงอุณหภูมิ
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return value * 9/5 + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value  # ไม่ต้องแปลงถ้าหน่วยเหมือนกัน

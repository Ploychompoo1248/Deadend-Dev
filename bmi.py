from pyscript import when
from pyscript.web import page 
# Define constants for BMI categories and thresholds
BMI_CATEGORIES = {
    "underweight": "น้ำหนักน้อย / ผอมเกินไป",
    "normal": "ปกติ (สุขภาพดี)",
    "overweight": "อ้วน",
    "obese": "อ้วนมาก"
}

BMI_THRESHOLDS = {
    "underweight": 18.60,
    "normal": 24.99,
    "overweight": 29.99
}

def calculate_bmi(weight: float, height: float) -> dict:
    """Calculate BMI and determine health status."""
    if height <= 0:
        print("Height must be greater than zero.")
    if weight <= 0:
        print("Weight must be greater than zero.")
    
    bmi_value = weight / (height ** 2)
    status = ""

    if bmi_value < BMI_THRESHOLDS["underweight"]:
        status = BMI_CATEGORIES["underweight"]
    elif BMI_THRESHOLDS["underweight"] <= bmi_value <= BMI_THRESHOLDS["normal"]:
        status = BMI_CATEGORIES["normal"]
    elif BMI_THRESHOLDS["normal"] < bmi_value <= BMI_THRESHOLDS["overweight"]:
        status = BMI_CATEGORIES["overweight"]
    else:
        status = BMI_CATEGORIES["obese"]

    return {"bmi": bmi_value, "status": status}

btn = page['#calculate-button']
@when('click',btn)
def calculate_and_display_bmi(_event):
    """Retrieve input values and display the BMI result."""
    weight = float(page['#weight'].value[0])
    height = float(page['#height'].value[0])
    print(weight,height)
    result = calculate_bmi(weight, height)
    print(result)
    # Display the result on the webpage
    if result["bmi"] is not None:
        message = f"BMI: {result['bmi']:.2f}, Status: {result['status']}"
    else:
        message = result["status"]
    print(message)
    page['#result'].innerText = message

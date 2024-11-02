from flask import Flask, jsonify, request
from flask import abort

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
        abort(400, description="Height must be greater than zero.")
    if weight <= 0:
        abort(400, description="Weight must be greater than zero.")
    
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

app = Flask(__name__)
# Enable CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route('/bmi', methods=['GET'])
def bmi():
    """GET route to calculate BMI."""
    try:
        weight = float(request.args.get('weight'))
        height = float(request.args.get('height'))
    except (TypeError, ValueError):
        abort(400, description="Invalid weight or height provided.")

    bmi_result = calculate_bmi(weight, height)
    return jsonify({'bmi': round(bmi_result['bmi'], 2), 'status': bmi_result['status']}), 200

if __name__ == '__main__':
    app.run(debug=True)
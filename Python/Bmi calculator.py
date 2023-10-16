def determine_weight_status(weight, height):
    bmi = weight / (height * height)
    if bmi < 16.0:
        return "severely underweight"
    elif 16.0 <= bmi < 16.9:
        return "very underweight"
    elif 17.0 <= bmi < 18.4:
        return "moderately underweight"
    elif 18.5 <= bmi < 24.9:
        return "normal weight"
    elif 25.0 <= bmi < 29.9:
        return "overweight"
    elif 30.0 <= bmi < 34.9:
        return "obese class 1 (Moderate)"
    elif 35.0 <= bmi < 39.9:
        return "obese class 2 (Severe)"
    else:
        return "obese class 3 (Very Severe)"

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

status = determine_weight_status(weight, height)
print(f"You are {status}.")


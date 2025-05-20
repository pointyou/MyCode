"""BMI calculation."""

def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    if height_cm <= 0:
        raise ValueError("身高需大於 0")
    return weight_kg / ((height_cm / 100) ** 2)

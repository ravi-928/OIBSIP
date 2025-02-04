def cal_bmi(weight, height):
    return weight / (height ** 2)

def catg_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return

        bmi = cal_bmi(weight, height)
        category = catg_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()

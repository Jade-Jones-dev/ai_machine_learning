# BMI calculator

def get_bmi(height, weight):
    height = float(height)
    weight = float(weight)
    bmi = weight / (height * height)
    bmi = round(bmi, 1)
    print(f"Your bmi is {bmi}")
    return bmi

def get_bmi_int(bmi):
    if bmi < 18.5:
        print("You are classed as underweight")
    elif 18.4 <= bmi < 25:
        print("You are classed as a healthy weight")
    elif 25 <= bmi < 30:
        print("You are classed as overweight")
    else:
        print("You are classed as obese")

   
if __name__ == "__main__":
    height = input("What is your height in meters (eg 1.75): ")
    weight = input("What is your weight in kg? ")
    bmi = get_bmi(height, weight)
    get_bmi_int(bmi)






# bmi_calculator.py
# BMI Calculator program obtains user's name, 
# prompts user to choose the preferred units of measurement, 
# calculates user's Body Mass Index (BMI) and determines their BMI category.
# It also advises the user on how to maintain a healthy BMI.

# prompt for name and welcome user
name = input("Please enter your name: ")
print(f"Hi {name}, welcome to BMI Calculator.")

# prompt for user's preferred units 
unit = input("Choose your preferred unit of measure:" +
             "\n 1 - Standard\n 2 - Metric\n")

standard = '1'
metric = '2'
bmi = 0.0

while bmi == 0.0:
    if unit == standard:
        # read entered measurements in standard units and calculate BMI
        height = float(input("Enter your height in inches: "))
        weight = float(input("Enter your weight in pounds: "))
        bmi = weight / (height ** 2) * 703
    elif unit == metric:
        # read entered measurements in metric units and calculate BMI
        height = float(input("Enter your height in metres: "))
        weight = float(input("Enter your weight in kilograms: "))
        bmi = weight / (height ** 2)
    else:
        # user prompted to select units again as BMI isn't calculated yet
        unit = input("No such units of measurement. Please try again:\n" + 
              "(Use 1 for Standard or 2 for Metric)\n")

print(f"{name}, your BMI is: {round(bmi, 1)}\n")

# use the calculated BMI to output categories
if bmi <= 18.5:
    print("""You are underweight.
    Tips:
    - You may need to gain weight.
    - Ask your doctor if this is a healthy weight for you.""")
elif bmi <= 24.9:
    print("""You're at normal weight.
    Tips:
    - You have a healthy weight.
    - Try not to gain or lose weight.
    - Eat healthy and be physically active.""")
elif bmi <= 29.9:
    print("""You're overweight.
    Tips:
    - You may need to lose weight.
    - Talk to your doctor or dietitian about your health risks """ +
    """and if you might need to lose weight.""")
else:
    print("""You are obese.
    Tips:
    - You need to lose weight.
    - Talk to your doctor or dietitian about safe and effective """ +
    """ways to lose weight and keep it off.""")

# show BMI categories chart
print("\n\tBMI Categories Chart")
print("-" * 38)
print("* Underweight - less than 18.5")
print("* Normal      - between 18.5 and 24.9")
print("* Overweight  - between 25 and 29.9")
print("* Obese       - 30 or greater")
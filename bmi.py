height = float(input("How many inches tall are you?  "))
bmi_height = height * 0.0254
feet = height // 12
inches = height % 12

weight = float(input("How many pounds do you weigh?  "))
bmi_weight = weight * 0.45
BMI = bmi_weight/(bmi_height*bmi_height)

print(f"\nSo you are {int(feet)}' {int(inches)}'' and and weigh {int(weight)} pounds.")
print(f"\nThis means you weigh {round(bmi_weight,1)} kilograms and are {round(bmi_height*100,1)} centimeters tall.")
if BMI <= 25:
    health_index = 'healthy'
elif 25 < BMI < 30:
    health_index = 'overweight.  To be healthy, you must reduce your BMI to below 25.'
else:
    health_index = 'obese'

print(f"\nYour BMI is {round(BMI,1)}.  You are {health_index}.\n")
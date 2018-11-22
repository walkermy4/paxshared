age = input("How many years old are you?  ")

height = int(input("How many inches tall are you?  "))
bmi_height = height * 0.0254
feet = height // 12
inches = height % 12

weight = int(input("How many pounds do you weigh?  "))
bmi_weight = weight * 0.45
BMI = bmi_weight/(bmi_height*bmi_height)

print(f"\nSo you are {age} years old, {feet}' {inches}'', and weigh {weight} pounds.")
print(f"\nThis means you weigh {round(bmi_weight)} kilograms and are {round(bmi_height*100)} centimeters tall.")
if BMI <= 26:
    health_index = 'healthy'
elif 26 < BMI < 30:
    health_index = 'overweight'
else:
    health_index = 'obese'

print(f"\nThis also suggest that for your age and BMI, which is {round(BMI)}, you are {health_index}.\n")

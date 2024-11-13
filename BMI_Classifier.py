height = float(input("Enter Your Height in Meters : "))
weight = float(input("Enter Your Weight in Kg : "))
BMI = round(weight / height ** 2)
print("Body Mass Index (BMI) is equal to", BMI)

# classifies BMI into different Categories..
if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 24.9:
    print("Normal Weight and Healthy range")
elif 25 <= BMI < 29.9:
    print("Overweight")
elif 30 <= BMI < 34.9:
    print("Obesity Class I")
elif 35 <= BMI < 39.9:
    print("Obesity Class II")
elif BMI >= 40:
    print("Obesity Class III")
else:
    print("Invalid Data!")
print("Stay Fit and Healthy,Thank You !!")

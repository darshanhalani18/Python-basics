# Pizza Order Program.

print("Hello, Welcome to our Pizza Order Program!\n")
print("Please select the size of pizza you want :")
print("1.Small Pizza")
print("2.Medium Pizza")
print("3.Large Pizza")

size_choice = input("\nEnter Your Choice (1/2/3) : ")

price = 0
if size_choice == '1':
    price = 100
    size = 'Small'
elif size_choice == '2':
    price = 200
    size = 'Medium'
elif size_choice == '3':
    price = 300
    size = 'Large'
else:
    print("Invalid choice.Please restart the program and select a valid option.")
    exit()

extra_cheese = input("\nWould you like to add extra cheese? (Y/N): ")
if extra_cheese == 'Y' or extra_cheese == 'y':
    price += 30
extra_toppings = input("Would you like extra toppings? (Y/N): ")
if extra_toppings == 'Y' or extra_toppings == 'y':
    price += 40

print(f"\nYou have Ordered a {size} size Pizza")
if extra_cheese == 'Y' or extra_cheese == 'y':
    print("Added : Extra Cheese")
if extra_toppings == 'Y' or extra_toppings == 'y':
    print("Added : Extra Toppings")

print(f"\nTotal Price : {price}")
print("\nThank you for your Order! Your pizza will be ready soon.")

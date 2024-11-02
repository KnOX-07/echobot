water_intake = 0
while water_intake < 2000:
    user_input = input("Have you had any water since the last update? (yes/no): ")
    if user_input == "yes":
        amount = int(input("How many ounces? "))
        water_intake += amount
        print("Your current water intake is", water_intake, "ounces.")
    elif user_input == "no": 
        print("Keep drinking water! Your current intake is", water_intake, "ounces.")
    else: 
        print("Invalid input. Please enter 'yes' or 'no'.")
print("Congratulations! You have reached your daily water intake goal of 2000 ounces.")
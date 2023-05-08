# This is a program that allows user to input the type of calculation they want to perform
# They have the option to select if they want to calculate interest of their investment or EMI of their bond

import math

print ("investment - to calculate the amount of interest you'll earn on your investment")
print ("bond - to calculate the amount you'll have to pay on a home loan")

# Here the user makes the selection. They can type their selection in all uppercase, initial uppercase or all lowercase
menu_select = input("Enter either 'investment' or 'bond' from the above to proceed: ").lower()

if menu_select == "investment":
    principle = float(input("Please enter the amount you want to deposit: "))
    interest_rate = float(input("Please enter the rate of interest (in percentage): "))
    time = float(input("Please enter the no. of years you plan on investing: "))
    interest_type = input("Do you want simple or compound interest? ").lower()

    # Used nested if statements to further divide their selection
    if interest_type == "simple":
        total = principle * (1 + (interest_rate/100) * time)
    elif interest_type == "compound":
        total = principle * math.pow(1 + (interest_rate/100), time)
    else:
        print("Invalid option selected")
        exit()

    print(f"Your amount of {principle} at the interest rate of {interest_rate}% after {time} year/s will be: {total}")

elif menu_select == "bond":
    property_value = float(input("Please enter the present calue of the property: "))
    interest_rate = float(input("Enter the interest rate charged: "))
    time = float(input("Enter the number of months you plan to take to repay the bond: "))
    interest_rate = (interest_rate / 12) / 100

    total = (interest_rate * property_value) / (1 - (1 + interest_rate)**(-time))

    print(f'The amount you have to pay each month is: {total}')

else:
    print("Invalid option selected.")
    exit()
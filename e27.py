#define a function as per below requirement
# 1. takes a temperature as input
# 2. returns hot if temp is greater than 25
# 3. returns warm if temp is between 15 and 25
# 4. returns cold if temp is less than 15

def temp(tmp):
    if tmp > 25:
        return "hot"
    elif 25 >= tmp >= 15:
        return "warm"
    else: 
        return "cold"
user_input = int(input("Enter temperature:"))

print(temp(user_input))
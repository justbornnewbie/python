#define a function as per below requirement
# 1. takes a temperature as input
# 2. returns Warm if temp is greater than 7
# 3. returns Cold if temp is equal or less than 7

def temp(tmp):
    if tmp > 7:
        return "warm"
    else:
        return "cold"

print(temp(10))
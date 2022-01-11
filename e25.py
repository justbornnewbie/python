#create a function with below requirements
#1.takes a string as a parameter
#2.returns false if the string contains less than 8 characters
#3. returns true if the string contains 8 or more characters

def length_cal(length):
    if len(length) >= 8:
        return True
    else:
        return False

length_cal("test")
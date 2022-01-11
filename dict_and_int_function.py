#take dictionary value as input in function and then add it
def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
        
    return the_mean

student_grades = {"Marry": 9.1, "Shim": 7, "John": 9.5}
print(mean(student_grades))
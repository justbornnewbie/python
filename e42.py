#convert lower case list strings to upper case by creating function
def case_change(*args):
    args = [x.upper() for x in args]
    return sorted(args)

print(case_change("rahul","jaysingh","maurya"))
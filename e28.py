#implement a function to take a name as input and print as "Hello Name"
def name(ename):
    fname = input("Please enter your name: ")
    message = "Hello %s" % (fname)
    return message
print(name("rahul"))
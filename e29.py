#implement a function to take a name as input and print as "Hello Name" Name's first letter should be in capital
def name(ename):
    fname = input("Please enter your name: ")
    message = "Hello %s" % (fname)
    return message.title()
print(name("rahul"))
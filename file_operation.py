myfile = open("fruits.txt")
print(myfile.read())
print(myfile.read())


with open("fruits.txt") as myfiles:
    contents = myfiles.read()
print(contents)
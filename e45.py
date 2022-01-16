#read the text from fruits.txt file and print out the first 20 characters of its content
with open("fruits.txt") as myfile:
    content = myfile.read()
print(content[:20])
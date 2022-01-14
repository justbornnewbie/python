#read the text from bear.txt file and print out the first 90 characters of its content
with open("fruits.txt") as myfile:
    content = myfile.read()
print(content[:10])
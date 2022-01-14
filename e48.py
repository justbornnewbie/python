#create first.txt file that contains first 20 characters of fruits.txt file
with open("fruits.txt") as file:
    content = file.read()

with open("first.txt", "w") as myfile:
    myfile.write(content[:20])

with open("fruits.txt", "a+") as myfile1:
    myfile1.write("\nbanana")
    myfile1.seek(0)
    content1 = myfile1.read()

print(content1)
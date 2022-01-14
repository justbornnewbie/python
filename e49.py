#append the text of bear1.txt to bear2.txt. in other words, bear2.txt should contain its text and the text of bear1.txt after that
with open("bear1.txt") as file1:
    content = file1.read()

with open("bear2.txt", "a") as file2:
    file2.write(content)
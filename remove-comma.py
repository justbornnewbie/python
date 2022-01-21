with open("comma.txt",'r') as file:
    data=file.read()
    data=data.replace(","," ")

with open ("comma-file.txt", 'w') as file:
    file.write(data)

print("Text Replaced")


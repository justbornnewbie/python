import time
while True:
    with open("fruits.txt") as file:
        print(file.read())
        time.sleep(3)
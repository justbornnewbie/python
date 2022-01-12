#loop over only integer big numbers
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for col in colors:
    if isinstance(col, int):
        if col > 50:
            print(col)
#define a function that gets a single string character and a filepath as parameters and returns the number of occurences of that character in the file.
def foo(character, filepath="fruits.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)
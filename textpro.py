def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    if phrase.startswith(("How", "what", "why", "when")):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_input = input("Say Something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))
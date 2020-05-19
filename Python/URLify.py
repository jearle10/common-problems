#! usr/bin/env python3

print("URLify")

# o(n) time and o(n) space


def urlify(string):
    char = []
    for letter in string:
        if letter == " ":
            char.append("%20")
        else:
            char.append(letter)
    output = ""
    for x in char:
        output += x

    print(output)


urlify("Hello amy name is Jian")

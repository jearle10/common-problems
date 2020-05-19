

# o(n^2) time and o(n) space

def compressed(string):
    charCount = {}
    compressed = ""
    for letter in string:
        if letter in charCount:
            charCount[letter] += 1
        else:
            charCount[letter] = 1

    for letter in charCount:
        compressed += letter + str(charCount[letter])

    if len(compressed) > len(string):
        return string
    else:
        return compressed


print(compressed("Hlll"))

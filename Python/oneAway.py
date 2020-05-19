
# insert, remove , replace are the three different kinds of changes this algo caters for


# For either string to be 'one away' from the other it would require it to be


def oneAway(string1, string2):
    [charCount1, charCount2] = countChar(string1, string2)
    difference = {}
    diffCount = 0

    if lengthCheck(string1, string2) == False:
        return False
    elif lengthCheck(string1, string2) > 0 or lengthCheck(string1, string2) < 0:
        diffCount += 1

    for letter in charCount1:
        if letter in charCount2:
            difference[letter] = charCount1[letter] - charCount2[letter]
            if difference[letter] != 0:
                diffCount += 1
        else:
            diffCount += 1

    if diffCount > 1:
        return False
    else:
        return True


def countChar(string1, string2):
    charCount1 = {}
    charCount2 = {}

    for letter1 in string1:
        if letter1 in charCount1:
            charCount1[letter1] += 1
        else:
            charCount1[letter1] = 1

    for letter2 in string2:
        if letter2 in charCount2:
            charCount2[letter2] += 1
        else:
            charCount2[letter2] = 1

    return [charCount1, charCount2]


def lengthCheck(string1, string2):
    if len(string1) - len(string2) < -1 or len(string1) - len(string2) > 1:
        return False
    else:
        return len(string1) - len(string2)


# print(countChar("hello", "test"))


print("LENGTH CHECK:", lengthCheck("Hello", "hellllo"))
print(oneAway("Heleoo", "Hello"))

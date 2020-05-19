

# o(n) time complexity o(n) space

def countChar(string):
    charCount = {}
    for letter in string.lower():
        if letter in charCount:
            if letter != " ":
                charCount[letter] += 1
        else:
            if letter != " ":
                charCount[letter] = 1
    return charCount

# o(n) time complexity o(n) space


def trim(string):
    concat = []
    for letter in string:
        if letter != " ":
            concat.append(letter)
    return concat


# o(n) time complexity o(1) space

def checkOdd(string):
    charCount = countChar(string)
    print("checked odd")
    SingleOddCheck = False
    for letter in charCount:
        if SingleOddCheck == True and charCount[letter] % 2 == 1:
            return False
        if charCount[letter] == 1:
            SingleOddCheck = True
    return SingleOddCheck

# o(n) time complexity o(1) space


def checkEven(string):
    charCount = countChar(string)
    print("checked even")
    allEvenCheck = True
    for letter in charCount:
        if charCount[letter] % 2 > 1 or charCount[letter] == 1:
            return False
    return allEvenCheck


# o(n) time complexity o(n) space

def PalindromeCheck(string):
    charCount = countChar(string)
    length = trim(string)
    for letter in charCount:
        if charCount[letter] == len(length):
            return True
    if len(length) == 0:
        return False
    if len(length) % 2 == 0:
        result = checkEven(string)
    else:
        result = checkOdd(string)
    return result


print(PalindromeCheck("ee eee "))

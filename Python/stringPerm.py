

# o(n) time o(n) space


def checkPerm(string1, string2):
    if len(string1) != len(string2):
        return False

    count = {}
    for letter in string1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for x in string2:
        if x in count:
            count[x] -= 1
            if count[x] < 0:
                return False
        else:
            count[x] = - 1
            if count[x] < 0:
                return False

    print(count)
    return True


print(checkPerm("hrllo", "hello"))



# O(n^2) Time complexity O(1) space


def unique1(string):
    i = 0
    while i < len(string):
        for letter in string[i+1: len(string)]:
            print(letter)
            if letter == string[i]:
                print("FOUND DUPPLICATE LETTERS")
                return
        i += 1
    print("NO DUPLICATES FOUND")


# O(n) Time complexity O(n) space

def unique2(string):
    hash = {}
    for letter in string:
        if letter in hash:
            print("FOUND DUPPLICATE LETTERS")
            return False

        hash[letter] = True
    print("NO DUPLICATES FOUND")
    return True

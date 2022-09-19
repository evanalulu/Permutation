""" Check Permutation: Given two strings, write a method to decide
if one is a permutation of the other. """

strOne = "hello"
strTwo = "olluh"

def isPermutation(strOne, strTwo):
    # Edge case
    if (len(strOne) != len(strTwo)):
        return False

    letters = {}
    for char in strOne:
      if (char in letters):
        letters[char] += 1
      else:
        letters[char] = 1

    for char in strTwo:
      if (char in letters):
        letters[char] -= 1
      else:
        return False

    for char in letters:
        if (letters[char] != 0):
            return False
          
    return True

print(isPermutation(strOne, strTwo))

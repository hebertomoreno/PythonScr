import re
def palindromeRearranging(inputString):
    repeatedReg = re.compile("(\\w)\\1")
    inputString = sorted(list(inputString))
    inputString = ''.join(inputString)
    inputString = re.sub(repeatedReg, '',inputString)
    if(len(inputString) <= 1):
        return True
    return False

print(palindromeRearranging("kayak"))
print(palindromeRearranging("aaaaa"))
print(palindromeRearranging("aabbcc"))
print(palindromeRearranging("president"))
print(palindromeRearranging("a"))
print(palindromeRearranging("bbbaaacc"))
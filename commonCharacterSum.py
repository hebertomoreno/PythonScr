def commonCharacterCount(s1, s2):
    commonCharSum = 0
    checkedLetters = []
    for letter in s1:
        if letter not in checkedLetters:
            commonCharSum += min(s1.count(letter),s2.count(letter))
            checkedLetters.append(letter)
    return commonCharSum
        
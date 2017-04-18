number = input()
newString = []
for char in number:
    if char != "9":
        char = str(int(char) + 1)
        newString.append(char)
    else:
        char = "0"
        newString.append(char)
   
print(''.join(newString))
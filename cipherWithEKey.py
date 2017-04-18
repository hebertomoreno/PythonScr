number = input()
eKey = int(input())
newString = []
for char in number:
    char = int(char)+eKey
    if(char>9):
        char = char - 10
    newString.append(str(char))

print(''.join(newString))
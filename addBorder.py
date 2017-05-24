def addBorder(picture):
    lengthOfRect = len(picture[0])
    newPicture = []
    astTop = '*' * lengthOfRect
    astTop = astTop + '**'
    for elem in picture:
        elem = list(elem)
        elem.insert(0,'*')
        elem.append('*')
        elem = ''.join(elem)
        newPicture.append(elem)
    newPicture.insert(0,astTop)
    newPicture.append(astTop)
    return newPicture

picture = ['abc','ded']

print(addBorder(picture))
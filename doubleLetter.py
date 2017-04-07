import re

s = input().strip()
regex = re.compile(r'(\w)(\1)')

match = regex.search(s)

while match:    
    s = s.replace(match.group(),'')        
    match = regex.search(s)

if(s):
	print(s)
else:
	print("Empty String")
#import the Regex module
import re

#Create a Regex object with a raw string (r'')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#Pass the string you want to search
#Returns a Match object
mo = phoneNumRegex.search('My number is 415-555-4242.')
#Call the Match object´s group() method
print('Phone number found: ' + mo.group())

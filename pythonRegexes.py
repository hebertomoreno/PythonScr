#\d is any digit, that is
#it is shorthand for the regular expression
#(0|1|2|3|4|5|6|7|8|9)
#\D is any character that is NOT a numeric digit from 0-9
#\w is any letter, numeric digit, or the underscore.
#\W any character that is NOT a letter, numeric digit, or the underscore.
#\s Any space, tab or newline char. 
#\S Any character that is NOT a space, tab or newline
#[0-5] Character class that matches only the numbers 0-5

#Catches a phone number with hyphens
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex = re.compile(r'(\d){3}-(\d){3}-(\d){4}')

#Catches a phone number  wrapping the area code and the number in two groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

#Catches a phone number INCLUDING parentheses, also two groups
phoneNumRegex = re.compile(r'(\(\d\d\d\))(\d\d\d-\d\d\d\d)')

#The string 'Batman' or the string 'Tina Fey' 
heroRegex = re.compile(r'Batman|Tina Fey')

#'Bat' followed by either man, mobile, copter or bat
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

#The question mark after the group to be searched indicates
#That the item may or may not be there
#'Bat' then zero or one times 'wo' then man
#Catches 'Batman' and 'Batwoman'
batRegex = re.compile(r'Bat(wo)?man')

#Phone number with or without area code
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

#'Bat' followed by zero or MORE 'wo' then 'man'
batRegex = re.compile(r'Bat(wo)*man')

#'Bat' followed by one or more 'wo' then 'man'
batRegex = re.compile(r'Bat(wo)+man')

#Three 'Ha's
haRegex = re.compile(r'(Ha){3}')

#Matches the longest string possible of 3 to 5 'Ha's
greedyHaRegex = re.compile(r'(Ha){3,5}')
#Matches the shortest string possible of 3 to 5 'Ha's
#Note that the question mark in this case declares nongreediness
nongreedyHaRegex = re.compiler(r'(Ha){3,5}?')
#Character class for catching vowels
vowelRegex = re.compile(r'[aeiouAEIOU]')
#All lowercase, Uppercase letters and numbers
letterRegex = re.compile(r'[a-zA-Z0-9]')
#Inside brackets, the period is interpreted as such. 
#This catches numbers 0-5 and a period
periodRegex = re.compule(r'[0-5.]')
#Adding ^just after the character class opening bracket, makes this a 
#negative character class, and matches all the characters that are
#not in the character class. 
consonantRegex = re.compile(r'[^aeiouAEIOU]')
#NOTE the caret symbol (^) can also be used at the start of a regex
#to indicate that a match must occur at the beginning of the searched
#text. 
#Matches strings that begin with hello
beginsWithHello = re.compile(r'^Hello')
#In the same way, ($) can be used to indicate that the string must
#end with the regex pattern
#Matches a string that ends with a number
endsWithNumber = re.compile(r'\d$')
#The (.) character is used as a wildcard and will match any 
#character except for a newline
#Matches any three character string that ends with 'at'
atRegex = re.compile(r'.at')
#(.*) is used to match everything and everything
#This matches everything after First name and Last Name
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
#The DOTALL argument makes the dot character match all characters
#including the newline character
newLineRegex = re.compile('.*', re.DOTALL)
#NOTE Remember the regexes are case sensitive
#To make a regex case insensitive pass re.IGNORECASE 
#or re.I as a second argument
robocopRegex = re.compile(r'robocop', re.I)
#The sub() method for Regex objects is passed to replace found
#occurences with another string
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
#Use a number and a slash (\1, \2) to replace part of the 
#Found text in the substitution, but replace the rest.
#The number is the group number to keep in.
agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1*****', 'Agent Alice is Agent Carol.')
#When writing very long and multiple lined Regexes, 
#The argument re.VERBOSE can be passed to the regex 
#The thriple quotes (''') are used to create a multiline string
phoneRegex = re.compile(r'''(
	(\d{3}|\(d{3}\))?
	)''', re.VERBOSE)
#Second arguments are combined using the (|) 
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE )
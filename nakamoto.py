# Automate the boring stuff with python
# Practice Question 21
# Page 171

# How would you write a regex that matches the full name of someone
# whose last name is Nakamoto? You can assume that the first name that
# comes before it will always be one word that begins with a capital letter.



#Import the re module
import re

nakamotoRegex = re.compile(r'''(
	[A-Z]			# One capital Letter
	[a-z]+			# One or more lowercase letters
	\s				# a space
	(Nakamoto)      #The lastname Nakamoto
	)''', re.VERBOSE)

mo = nakamotoRegex.search('satoshi Nakamoto')
print('Name found: ' + mo.group())
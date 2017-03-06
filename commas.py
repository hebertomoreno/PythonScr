import re

numberRegex = re.compile(r'''(
	[^0-9]*
	(\d{1,3},)?
	(\d{1,3}\s)
	)''',re.VERBOSE)

matches = []
for groups in numberRegex.findall('555 8963 789,558 256, 596,568,895'):
	matches.append(groups[0])

if len(matches) > 0:
	print('Numbers found:')
	print('\n'.join(matches))
else:
	print('No compatible numbers found.')
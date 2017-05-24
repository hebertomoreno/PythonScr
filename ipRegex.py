import re

def isIPv4Address(inputString):
	ipRegex = re.compile(r'^(\d{1,3}?)\.(\d{1,3}?)\.(\d{1,3}?)\.(\d{1,3}?)$')
	mo = ipRegex.search(inputString)
	if(mo):
		for group in mo.groups():
			if(int(group) > 255):
				return False
		return True
	return False
	
print(isIPv4Address("1.1.1.1.1"))
print(isIPv4Address('1.1.1.1a'))
print(isIPv4Address('130.220.23.12'))
print(isIPv4Address('122.350.1.12'))
print(isIPv4Address('1234.235.2345.2344'))
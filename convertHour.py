import re

hour = input()

indRegex = re.compile(r'(\d\d)(PM|AM)')
mo = indRegex.search(hour)
sec, ampm = mo.groups()

hour = hour.split(":")

if(ampm == "PM" and hour[0]!="12"):
	hour[0]= int(hour[0])+12
	hour[0] = str(hour[0])
elif(ampm=="AM" and hour[0]=="12"):
	hour[0] = "00"
hour[2] = sec
hour = ":".join(hour)
print(hour)
import webbrowser, requests, bs4, sys
from unidecode import unidecode

if len(sys.argv) == 2:
	# Get address from command line.
	state = ''.join(sys.argv[1:]).lower()
elif len(sys.argv) > 2:
	# If the state has more than one word in it, 
	# join it with a '-' which follows the format
	# of the page's url. 
	state = '-'.join(sys.argv[1:]).lower()
	state = unidecode(state) 

# Open the heraldo page for the state specified in the arguments
# webbrowser.open('http://heraldo.com.mx/'+state+'/')
# Get the heraldo page corresponding to the state
res = requests.get('http://heraldo.com.mx/'+state+'/municipios/')

# If the page isnt found, tell us so
res.raise_for_status()

# Store the webpage text in a variable
heraldoSoup = bs4.BeautifulSoup(res.text, 'html.parser')

# Select all the municipios (which are selected by their
# class, which in the heraldo page is either .fila_par
# or .fila_non)
muns = heraldoSoup.select('.fila_par,.fila_non')

# Cycle through the municipios 
for mun in muns:
	# Save the original name of the municipio in a variable, so we can compare it to 
	# the json later. 
	muniName = mun.getText()

	# In the classes selected, we can also find letters indicating each alphabetical section. 
	# There is no class specific to the municipios, so we get the length of the text to 
	# check if it is a municipio. There are no municipios with just one letter, as far as
	# I know. 
	if(len(mun.getText())) != 2:

		# Replace the spaces with dashes and move everything to a lowercase, according to
		# the naming format of the page. Consider changing the join above for a replace
		# when you're done writing the program. 
		muniParsedName = mun.getText().replace(' ','-').lower()

		# Unidecode gets a string and translates it to the nearest ASCII representation. 
		# The heraldo URL's do not contain accents, so this translates the accents into
		# its ASCII equivalent. 
		muniParsedName = unidecode(muniParsedName)

		print(muniName)
		# Request the municipio page and check for 404's using the parsed name.
		cpRes = requests.get('http://heraldo.com.mx/'+state+'/'+ muniParsedName+'/')
		res.raise_for_status()

		# Get the text for the webpage and select only the tags with a CP inside them. 
		cpSoup = bs4.BeautifulSoup(cpRes.text, 'html.parser')
		codigos = cpSoup.select('.codigo_par,.codigo_non')

		# Print the zipcodes. 
		for codigo in codigos:
			codigoText = codigo.getText()
			
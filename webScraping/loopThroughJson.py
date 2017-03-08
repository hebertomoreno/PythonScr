import csv,json
from unidecode import unidecode

# Open the Json file
exampleFile = open('son.json')

# Open the csv file to write
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

# Load the json file into a variable
# json.load is used here so that we can input a file. 
# Usually, json.loads is used, but it does not accept a file. 
loadedJson = json.load(exampleFile)

# Write the header row. 
outputWriter.writerow(['CVEGEO','Nombre'])

# Loop through each item in the json 'features', because it is GeoJSON
for item in loadedJson['features']:
	# Save the stringified values in variables. 
	CVEGEO = item['properties']['CVEGEO']
	nombreMun = item['properties']['NOMBRE']

	# print the CVEGEO and the name of the municipio, which is json.features[i].properties.NOMBRE
	print(CVEGEO, nombreMun)
	# Write a new row in the CSV
	outputWriter.writerow([CVEGEO, nombreMun])
# Open the file 'output.csv' in write mode. 
# If you forget the newline='' argument, the csv will be double spaced. 
outputFile = open('output.csv', 'w', newline='')

outputWriter = csv.writer(outputFile)

outputWriter.writerow(['spam', 'eggs', 'bacon','ham'])
outputWriter.writerow(['Hello, world!','eggs','bacon','ham'])
outputWriter.writerow([1,2,3.141516,4])

# Close the file. 
outputFile.close()
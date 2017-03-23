import pandas as pd

#orders = pd.read_table('http://bit.ly/chiporders')
orders =pd.read_table('territoryRef.csv', sep=',')

#print(orders.head())
#print(orders.describe())

orders['idWNameSSP'] = orders['SSP#'] + ',' + orders.SSP

print(orders.head())
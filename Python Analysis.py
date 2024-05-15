import pandas as pd

## import csv files as dataframes
detail = pd.read_csv('Raw Data/detail.csv')
menu = pd.read_csv('Raw Data/menu.csv')
order = pd.read_csv('Raw Data/order.csv')

# preview first five rows of each df
print(detail.head(5))
print(menu.head(5))
print(order.head(5))

print(detail.dtypes)
print(menu.dtypes)
print(order.dtypes)
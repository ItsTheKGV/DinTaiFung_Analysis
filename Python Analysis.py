# %%
import pandas as pd
import numpy as np
import matplotlib as mp
import seaborn as sb

# %%
## import csv files as dataframes
detail = pd.read_csv('Raw Data/detail.csv')
menu = pd.read_csv('Raw Data/menu.csv')
order = pd.read_csv('Raw Data/order.csv')

# %%
# preview first five rows of each df
print(detail.head(5))
print(menu.head(5))
print(order.head(5))

print(detail.dtypes)
print(menu.dtypes)
print(order.dtypes)

detail = detail.rename(columns={"item_id":"product_id"})
detailed_orders = detail.merge(menu, how = "inner", on = "product_id")
detailed_orders = detailed_orders.drop(columns=["price_x"])
detailed_orders = detailed_orders.rename(columns={"price_y":"price"})
print(detailed_orders.head(10))

# %%
sb.lineplot(order, x = "date", y = "total")
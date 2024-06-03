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

# %%
detailed_orders = detailed_orders.merge(order, how = "inner", on = "order_id")

# %%
detailed_orders = detailed_orders.drop(columns=["date_y"])
print(detailed_orders.head(10))

# %%
sb.lineplot(detailed_orders, x = "date", y = "total", hue = "category")

# %%
detailed_orders['date'] = pd.to_datetime(detailed_orders['date'])
detailed_orders['month'] = detailed_orders['date'].dt.to_period('M')

monthly_total = detailed_orders.groupby('month')['total'].sum().reset_index()
print("Monthly Totals:")
print(monthly_total)

# %%
sb.set(style="whitegrid")

sb.lineplot(x=monthly_total['month'].astype(str), y = monthly_total['total'],marker = 'o')

mp.title("Total by Month")
mp.xlabel("Month")
mp.ylabel("Total")
mp.xticks(rotation=45)
mp.grid(True)

mp.show()

# %%
filename = "Combined_Data.csv"
file_path = os.path.join("B:\Microsoft VS Code\Project Locations\DinTaiFung_Analysis\Processed Data", filename)

detailed_orders.to_csv(file_path, index=False)
print(f'DataFrame saved to {file_path}')
# %%

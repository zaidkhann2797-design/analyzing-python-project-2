import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Warehouse_and_Retail_Sales.csv")
print(df.head())

print(df.isnull().sum())

print(df.shape)

df.fillna("0",inplace=True)

df = df.drop_duplicates()

grouped = df.groupby("MONTH")["WAREHOUSE SALES"].sum()

bars = plt.bar(grouped.index, grouped.values, color="orange")
 
plt.title("warehouse sales by month")
plt.xlabel("month")
plt.ylabel("warehouse sales")
plt.xticks(rotation=45)

plt.bar_label(bars, label_type="edge")

plt.show()




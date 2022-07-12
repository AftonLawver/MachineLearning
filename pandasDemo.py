import pandas as pd

url = "datasets/automobiles.data"
df = pd.read_csv(url)
print(df.head())


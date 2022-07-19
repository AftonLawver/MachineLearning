import pandas as pd


url = "datasets/adult.data"
columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
           'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
           'hours-per-week', 'native-country', 'salary']
df = pd.read_csv(url, names=columns, index_col=0)


# df = df[['age', 'workclass', 'education', 'marital-status', 'occupation', 'relationship',
#         'race', 'sex', 'native-country']]

print(df.head(10))

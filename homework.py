import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data.head())
for category in data['whoAmI'].unique():
    data[category] = (data['whoAmI'] == category).astype(int)
data.drop('whoAmI', axis=1, inplace=True)
print(data.head())

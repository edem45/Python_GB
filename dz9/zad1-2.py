import pandas as pd

file_path = '/content/sample_data/california_housing_train.csv'
df = pd.read_csv(file_path, sep=',')

df['population'].min()


df[df['population'] < 500].median_house_value.mean()


df[df['population'] == df['population'].min()].households.max()
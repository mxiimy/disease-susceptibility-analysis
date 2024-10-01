import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("global air pollution dataset.csv")
print(df.columns)
def get_pollution(country):
    a = []
    i = 0
    for index, row in df.iterrows():
            # a[3,5,7,9,11]
        # print(row)
        i += 1
        print(df.loc[i, 'Country'])
        if df.loc[i, 'Country'] == country:
            value1 = df.iloc[i, 2]
            value2 = df.iloc[i, 4]
            value3 = df.iloc[i, 6]
            value4 = df.iloc[i, 8]
            value5 = df.iloc[i, 10]
            a = [value1, value2, value3, value4, value5]
            return a
print(get_pollution('India'))




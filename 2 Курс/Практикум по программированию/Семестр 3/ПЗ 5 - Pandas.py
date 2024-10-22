import pandas as pd

data1 = {
    'Name': ['Strom, Mrs. Wilhelm (Elna Matilda Persson)',
             'Navratil, Mr. Michel ("Louis M Hoffman")',
             'Minahan, Miss. Daisy E'],
    'Age': [29, 36.5, 33],
    'Sex': ['female', 'male', 'female']
}
df1 = pd.DataFrame(data1)
print(df1.to_string())
input()

df2 = pd.read_csv('D:/GitHub/OmGTU/2 Курс/Практикум по программированию/Семестр 3/titanic_csv.csv', sep=";")
df2.columns = df2.columns.str.lower()
print(df2)
input()

df3 = pd.read_csv('https://gist.githubusercontent.com/zaryanezrya/8b4ef51c707cb16d5e88a44dc00a1bb2/raw/41230f49c6268e072dbf102672f670be256922ab/gistfile1.txt')
print(df3)
input()

comb_df = pd.concat([df2, df3]).drop_duplicates()
print(comb_df)
input()

comb_df.set_index('passengerid', inplace=True)
comb_df.sort_index(inplace=True)
print(comb_df)
input()

comb_df.info()
print(comb_df.describe())
input()

comb_df.iloc[0], comb_df.iloc[2] = comb_df.iloc[2], comb_df.iloc[0]
print(comb_df)
input()

comb_df['sex'] = comb_df['sex'].map({'female': 'f', 'male': 'm'})
print(comb_df.to_string())
input()

ticket_counts = comb_df.groupby('ticket').size()
large_groups = ticket_counts[ticket_counts >= 6]
people_in_large_groups = comb_df[comb_df['ticket'].isin(large_groups.index)]
print(people_in_large_groups)
input()

cabin_values = comb_df[comb_df['name'].isin(df1['Name'])]['cabin'].unique()
people_in_same_cabins = comb_df[comb_df['cabin'].isin(cabin_values)]
print(people_in_same_cabins)

comb_df['birthyear'] = 2024 - comb_df['age']
print(comb_df)
input()

comb_df['companions'] = comb_df.groupby('cabin')['name'].transform(lambda x: ', '.join(x[x != x.name]))
print(comb_df)
input()

comb_df.iloc[0], comb_df.iloc[1] = comb_df.iloc[1], comb_df.iloc[0]
print(comb_df)
input()

comb_df.to_csv('D:/GitHub/OmGTU/2 Курс/Практикум по программированию/Семестр 3/combined_passengers.csv', sep=";")
input()

top_10_paid = comb_df.nlargest(10, 'fare')
print(top_10_paid)
input()

survival_sex = comb_df.groupby(['sex', 'survived']).size()
print(survival_sex)
input()

survival_class = comb_df.groupby(['pclass', 'survived']).size()
print(survival_class)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import normaltest


# 3
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
df = pd.read_csv('laptop_price.csv')
print(df)
print("\nИнформация о датафрейме:")
print(df.info())
print("\nОсновная статистическая информация:")
print(df.describe())
df.drop_duplicates(inplace=True)
print("\nКоличество строк после удаления дубликатов:", df.shape[0])

# 4
df.rename(columns={'Weight (kg)': 'Weight_kg'}, inplace=True)
print("\nНовые названия колонок:")
print(df.columns)

# 5
plt.figure(figsize=(10, 6))
sns.histplot(df['Price (Euro)'], kde=True)
plt.title('Гистограмма распределения цен')
plt.savefig('histogram.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Price (Euro)'])
plt.title('Диаграмма ящика с усами для цен')
plt.savefig('boxplot.png')
plt.close()

plt.figure(figsize=(8, 8))
df['TypeName'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Распределение типов ноутбуков')
plt.savefig('pie_chart.png')
plt.close()

plt.figure(figsize=(12, 8))
numerical_df = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numerical_df.corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Тепловая карта корреляции')
plt.savefig('heatmap.png')
plt.close()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Company', hue='TypeName')
plt.title('Countplot для компаний и типов ноутбуков')
plt.xticks(rotation=45)
plt.savefig('countplot.png')
plt.close()

# 6
for column in df.columns:
    if df[column].isnull().sum() > 0:
        if pd.api.types.is_integer_dtype(df[column]):
            df[column].fillna(df[column].median(), inplace=True)
        elif pd.api.types.is_float_dtype(df[column]):
            df[column].fillna(df[column].mean(), inplace=True)
        else:
            df[column].fillna(df[column].mode()[0], inplace=True)
print(df.isnull().sum())

# 7
sample = df['Price (Euro)'].sample(n=200, random_state=42)
stat, p_value = normaltest(sample)
print('\nСтатистика распределения:', stat)
print('p-value:', p_value)

# 8
df = pd.get_dummies(df, drop_first=True)
print("\nФорма датафрейма после one-hot кодирования:", df.shape)
print(df)

# 9
df.to_csv('preprocessed_laptop_price.csv', index=False)

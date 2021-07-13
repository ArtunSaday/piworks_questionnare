import pandas as pd

df = pd.read_csv('country_vaccination_stats.csv')
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(df.groupby('country')['daily_vaccinations'].transform('min'))
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)
print('Top 3 countries with highest median daily vaccination numbers: ')
print(df.groupby(['country']).median().sort_values('daily_vaccinations', ascending=False)[0:3])
print(df.loc[df['date'] == '1/6/2021', 'daily_vaccinations'].sum())

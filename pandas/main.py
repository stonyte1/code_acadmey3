import pandas as pd
import numpy as np

df = pd.read_csv('pandas/miestai_isvalyti.csv')

df.set_index('Miestas', inplace=True)

print(df.head())

print(df.loc['Panevėžys', '1897'])

print(df[['2019', '1970', '1923']].head(10))

print(df.shape)

number = np.linspace(1, 103, 103)
number = number.astype(int)

df['nr'] = number

print(df[(df['nr']>29) & (df['nr']<40)])

df.drop('nr', axis=1, inplace=True)
print(df.head())

print(df[df['1959'] == 0])

print(df[df['1897']>df['2019']])

print(df[df['2019'] > df['2011']])

print(df[(df['1897'] > df['1923']) &
   (df['1923'] > df['1959']) &
   (df['1959'] > df['1979']) &
   (df['1979'] > df['1989']) &
   (df['1989'] > df['2001']) &
   (df['2001'] > df['2011']) &
   (df['2011'] > df['2019'])])

proc_skirtumas = ((df['2019'] - df['1989'])/df['1989'])*100
print(f'{proc_skirtumas.idxmax()}\t {int(proc_skirtumas.max())}%\n\
{proc_skirtumas.idxmin()}\t{int(proc_skirtumas.min())}%')


print(df.reset_index().head())
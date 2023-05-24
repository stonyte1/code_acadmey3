import numpy as np
import pandas as pd
import urllib.parse

# import lxml
# from sqlalchemy import create_engine

# def month_number(month):
#     months = {1: 'January',
#     2: 'February',
#     3: 'March',
#     4: 'April',
#     5: 'May',
#     6: 'June',
#     7: 'July',
#     8: 'August',
#     9: 'September',
#     10: 'October',
#     11: 'November',
#     12: 'December'
#     }
#     for key, value in months.items():
#         if value == month:
#             return key


# html = pd.read_html('https://work.studentnews.eu/s/3695/75547-European-countries-the-table-language-population-capital-currency-phone-code-internet-code.htm')

# data = html[1]
# # print(data)

# data.to_csv('pandas/countries.csv', index=False)
# data.to_excel('pandas/countries.xlsx', 'Sheet1', index=False)

# # engine = create_engine('sqlite:///pandas/countries.db')
# # data.to_sql('countries', con=engine, index=False)

# fires = pd.read_csv('pandas/top_20_CA_wildfires.csv')
# # print(fires)

# unique_count = len(fires['cause'].unique())

# cause = fires['cause'].value_counts()

# max_fires = fires['year'].value_counts().idxmax()

# fire_death = fires['deaths'].value_counts().drop(0).sum()

# sorted_by_year = fires.sort_values('year', ascending=False)
# fires['month'] = fires['month'].apply(month_number)
# print(fires.head())


url = 'https://lt.wikipedia.org/wiki/Sąrašas:Lietuvos_miestai_pagal_gyventojus'
encoded_url = urllib.parse.quote(url, safe=':/')

towns = pd.read_html(encoded_url)[0]
towns.set_index('Miestas', inplace=True)

col_list = towns.columns.tolist()

new_list = []
for item in col_list:
    fixed = item.replace('\xa0m.', '')
    new_list.append(fixed)

towns.columns = new_list

print(towns)

def to_number(num):
    final = ''
    if type(num) == int:
        return num
    else:
        for x in str(num):
            if x.isdecimal() or x == '.':
                final += x
        if len(final) > 0:
            return int(float(final))
        return int(0)

for year in new_list:
    year = str(year)
    towns[year] = towns[year].apply(to_number)   

print(towns)



# Excel funktioner i Python
# Tue Hellstern

# Moduler
import pandas as pd
import numpy as np
from datetime import date

# ************************ DATA ************************
# Studerende Data
studerende = [['A-2022-1', 'Ole', 'Hansen'], 
['A-2022-2', 'Pia', 'Rasmussen'],
['A-2022-3', 'Lis', 'Larsen'],
['A-2022-4', 'Kim', 'Olsen'],
['A-2022-5', 'Lars', 'Petersen']]

# Studerende Dataframe
studerende_data = pd.DataFrame(studerende,columns=['Studenter-id', 'Fornavn', 'Efternavn'])
print(studerende_data)

# Karakter Data
karakter = [['A-2022-1', 'Dansk', 4],
['A-2022-2', 'Matematik', 7],
['A-2022-1', 'Historie', 10],
['A-2022-5', 'Engelsk', 2],
['A-2022-1', 'Tysk', 7],
['A-2022-3', 'Dansk', 0],
['A-2022-1', 'Matematik', 12],
['A-2022-3', 'Historie', 2],
['A-2022-3', 'Engelsk', 0],
['A-2022-4', 'Tysk', 4],
['A-2022-3', 'Matematik', 0],
['A-2022-3', 'Historie', 10],
['A-2022-1', 'Engelsk', 0],
['A-2022-3', 'Tysk', 4]]

# Karakter Dataframe
karakter_data = pd.DataFrame(karakter, columns=['Studenter-id', 'Fag', 'Karakter'])
print(karakter_data)

# ************************ LOPSLAG > MERGE ************************
studerende_karakter = pd.merge(studerende_data, karakter_data, on="Studenter-id")
print(studerende_karakter)

# ************************* HVIS > WHERE **************************
studerende_karakter['Bestået'] = np.where(studerende_karakter['Karakter']<2,'Dumpet', 'Bestået')
print(studerende_karakter)

# ************************* Tekst **************************
navn = 'Hansen'

print(navn[:2])
print(navn[-4:])
print(navn[1:4])

# **************** Aggregations funktioner *****************
print('Maks: ', studerende_karakter['Karakter'].max())
print('Min: ', studerende_karakter['Karakter'].min())
print('Middel: ', studerende_karakter['Karakter'].mean())
print('Median: ', studerende_karakter['Karakter'].median())

# ************************* Dato **************************
dagsdato = date.today()

print('År:', dagsdato.year)
print('Måned:', dagsdato.month)
print('Dag:', dagsdato.day)
print('Ugedag US start søndag:', dagsdato.weekday())
print('Ugedag DK start mandag:', dagsdato.isoweekday())
print('Ugedag tekst:', dagsdato.strftime('%A'))
print('Uge nr.:', date.isocalendar(dagsdato)[1])
---
title: Python-alternativer til Excel-funktioner
image: /images/blog/excel-python.jpg
summary: Sammenligning af Excel funktioner og Python funktioner
date: 2022-08-06
categories:
- excel
- python
---

# Python-alternativer til Excel-funktioner
Python har mange af de sammen funktioner som du kender fra Excel.

Her er et par eksempler på nogle meget brugte Excel funktioner og den sammen funktion i Python.

- [LOPSLAG > PD.MERGE](#excel-vlookup--python-pdmerge)
- [HVIS > NP.WHERE](#excel-if--python-npwhere)
- [Tekst funktioner](#excel--python-tekst-udtræk)
- [Aggregations funktioner](#aggregations-funktioner)
- [Dato funktioner](#dato-funktioner)
- [Filer](#filer)

## Excel LOPSLAG > Python PD.MERGE
I Excel kan du bruge en lookup funktion som **LOPSLAG()** når du vil hente værdier fra en anden "*tabel*" og tilføje dem til den aktuelle "*tabel*".

Eksempel data er to "*tabeller*" med studerende og deres karakterer.

![](/static/images/blog/excel-python-funktioner-data.jpg)


Du vil gerne have tilføjet *Fornavn* og *Efternavn* til *Karakter oversigten*, hvilket du kan gøre med **LOPSLAG**:

    =LOPSLAG(opslagsværdi, tabelmatrix, kolonneindeks_nr, [intervalopslag])
    =LOPSLAG(B5; $B$5:$D$9; 2; FALSK)

![](/static/images/blog/excel-python-funktioner-data-2.jpg)

**Tip**: *Prøv den nye* **XOPSLAG**-*funktion, det er en forbedret version af LOPSLAG, der fungerer i en hvilken som helst retning og returnerer nøjagtige matches som standard, hvilket gør den nemmere og mere praktisk at bruge end LOPSLAG.*

I Python kan du bruge flette funktionen **PD.MERGE** fra *Pandas* til at gøre det samme:

    studerende_karakter = pd.merge(studerende_data, karakter_data, on="Studenter-id")

![](/static/images/blog/excel-python-funktioner-data-3.jpg)

Nogle af fordelene ved PD.MERGE er:

- PD.MERGE kan håndtere større datamængder end LOPSLAG
- PD.MERGE er hurtigere, hvis du har mange LOPSLAG funktioner vil det gøre dit Excel ark langsomt

## Excel HVIS > Python NP.WHERE 
**HVIS()** funktionen i Excel kan du bruge til at oprette betingede værdier.

    =HVIS(logisk_test; [værdi_hvis_sand]; [værdi_hvis_falsk])

Hvis du vil tilføje teksten "*Dumpet*" til en ny kolonne, hvis karakteren er under 2, kan du gøre det med **HVIS()** funktionen.

    =HVIS(D5>=2; "Bestået"; "Dumpet")

![](/static/images/blog/excel-python-funktioner-data-4.jpg)

I Python kan du gøre det sammen med **WHERE()** funktionen som du finder i **NUMPY** modulet.

    studerende_karakter['Bestået'] = np.where(studerende_karakter['Karakter']<2,'Dumpet', 'Bestået')

![](/static/images/blog/excel-python-funktioner-data-5.jpg)

Syntaksen på **WHERE()** er meget lig syntaksen på **HVIS()**

## Excel > Python tekst udtræk
Når du har behov for at udtrække data fra en tekst streng kan du i Excel bruge følgende funktioner:

- **VENSTRE()** - *=VENSTRE(B3; 2)*
- **HØJRE()** - *=HØJRE(B3;4)*
- **MIDT()** - *=MIDT(B3;2;3)*

![](/static/images/blog/excel-python-funktioner-data-6.jpg)

I Python kan du opnå det sammen med disse funktioner:

    navn = 'Hansen'
    print(navn[:2])
    print(navn[-4:])
    print(navn[1:4])

![](/static/images/blog/excel-python-funktioner-data-7.jpg)


## Aggregations funktioner
I Excel har vi adskillige aggregerings funktioner til at opsummere dataene, nogle af de mest almindelige er:

- MAKS
- MIN
- MIDDEL
- MEDIAN
- SUM

![](/static/images/blog/excel-python-funktioner-data-8.jpg)

De tilsvarende Python funktioner er:

    print('Maks: ', studerende_karakter['Karakter'].max())
    print('Min: ', studerende_karakter['Karakter'].min())
    print('Middel: ', studerende_karakter['Karakter'].mean())
    print('Median: ', studerende_karakter['Karakter'].median())

![](/static/images/blog/excel-python-funktioner-data-9.jpg)


## Dato funktioner
Excel har forskellige funktioner du kan bruge nåt du skal arbejder med datoer, nogle af de mest almindelige er:

- ÅR()
- MÅNED()
- DAG()
- UGEDAG()
- TEKST() *Ugedag som tekst*
- UGE.NR

![](/static/images/blog/excel-python-funktioner-data-11.jpg)

I Python skal du bruge:

    dagsdato = date.today()

    print('År:', dagsdato.year)
    print('Måned:', dagsdato.month)
    print('Dag:', dagsdato.day)
    print('Ugedag US start søndag:', dagsdato.weekday())
    print('Ugedag DK start mandag:', dagsdato.isoweekday())
    print('Ugedag tekst:', dagsdato.strftime('%A'))
    print('Uge nr.:', date.isocalendar(dagsdato)[1])

Der er forskel på ugedags nummer uge nummer i Danmark og USA. Derfor skal du bruge **isocalendar** når du vil have DK uge nr. 

## Filer
Du kan hente og selv prøve de forskellige funktioner med disse to filer:

- [excel-python-funktioner.xlsx](excel-python-funktioner.xlsx)
- [excel-python-funktioner.py](excel-python-funktioner.py)
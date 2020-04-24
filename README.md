# Appartment Price Scrapper

Realtime overview of appartment prices in Barcelona. Based on the Python library [Scrappy](https://scrapy.org/) for automated crawling of [Habitaclia](https://www.habitaclia.com/). 
### Customizable visualisation (ipython notebook) 
* [Rent](visualisationRent.ipynb)
* [Buy](visualisationRent.ipynb)

### Genearted databases 
* [DB-Rent](DB-Rent)
* [DB-Buy](DB-Buy)

The format of each data base file is as follows:

| Line        | Position 0          | Position 1   |   Position 2   | ...|   Position N   |
| --- | --- | --- | --- | --- | --- |
0  |  hist. bin 0 (\*) |  hist. bin 1 (\*)|  hist. bin 2 (\*)|  ... |  hist. bin N (\*)|
1 | YearMonthDay | Counts 0-1 | Counts 1-2 | ... |  Counts (N-1)-N|
2 | YearMonthDay | Counts 0-1 | Counts 1-2 | ... |  Counts (N-1)-N|
3 | YearMonthDay | Counts 0-1 | Counts 1-2 | ... |  Counts (N-1)-N|

(\*)
In units of (€/month) or (€) for DB-Rent and DB-Buy, respectively.

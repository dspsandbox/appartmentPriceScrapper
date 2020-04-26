# Appartment Price Scrapper

Realtime overview of appartment prices in Barcelona. Based on the Python library [Scrappy](https://scrapy.org/) for automated crawling of [Habitaclia](https://www.habitaclia.com/) and database (DB) generation. 

Have  a look and configure the interactive notebooks bellow!
### Database visualisation (histogram / temporal evolution) 
* _visualisationRent.ipynb_ ---> [Interactive Notebook](https://mybinder.org/v2/gh/dspsandbox/appartmentPriceScrapper/master?filepath=visualisationRent.ipynb) / [Source](visualisationRent.ipynb) 
* _visualisationBuy.ipynb_ ---> [Interactive Notebook](https://mybinder.org/v2/gh/dspsandbox/appartmentPriceScrapper/master?filepath=visualisationBuy.ipynb) / [Source](visualisationBuy.ipynb) 

### Database information
Location:
* _/DB-Rent_ ---> See DB content [here](DB-Rent)
* _/DB-Buy_ --->  See DB content [here](DB-Buy)

Format (of each database file):

| Line        | Position 0          | Position 1   |   Position 2   | ...|   Position N   |
| --- | --- | --- | --- | --- | --- |
| 0  |  Hist. bin 0 (\*) |  Hist. bin 1 (\*)|  Hist. bin 2 (\*)|  ... |  Hist. bin N (\*)|
| 1 | YearMonthDay | Counts 0-1 | Counts 1-2 | ... |  Counts (N-1)-N|
| 2 | YearMonthDay | Counts 0-1 | Counts 1-2 | ... |  Counts (N-1)-N|
| 3 | YearMonthDay | Counts 0-1 | Counts 1-2 | ... |  Counts (N-1)-N|
| ... | ... | ... | ... | ... | ... |

(\*)
In units of (€/month) or (€) for DB-Rent and DB-Buy, respectively.

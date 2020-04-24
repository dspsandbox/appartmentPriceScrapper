#!/bin/sh
scrapy crawl habitacliaRent
scrapy crawl habitacliaBuy
jupyter nbconvert   --execute visualisationRent.ipynb --inplace 
jupyter nbconvert   --execute visualisationBuy.ipynb --inplace 
git pull
git stage *
git commit -m "update"
git push
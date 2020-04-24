import scrapy
import re
import time
import datetime
import os
import numpy as np


class habitacliaRentSpider(scrapy.Spider):
    pathDB="DB-Rent"
    name = "habitacliaRent"
    start_urls = [
        'https://www.habitaclia.com/alquiler-barcelona.htm',
    ]
    date=int((datetime.datetime.now()).strftime("%Y%m%d"))
    nextUrl=None
    locationList=[]
    priceList=[]

    priceMin=0
    priceMax=10000
    priceBins=1000

    def parse(self, response):
        try:
            locationListPage=[]
            priceListPage=[]

            for listItem in response.xpath('//div[@class="list-item-info"]'):
                location=None
                price=None

                if len(listItem.xpath('.//p[@class="list-item-location"]/span/text()'))>0:
                    location=listItem.xpath('.//p[@class="list-item-location"]/span/text()')[0].get() 
                if len(listItem.xpath('.//article[@class="list-item-price"]/span[@itemprop="price"]/text()'))>0:
                    price= listItem.xpath('.//article[@class="list-item-price"]/span[@itemprop="price"]/text()')[0].get() 
                    price=int(price.replace("€","").replace(".",""))                
                if (location!=None) and (price!=None):
                    locationListPage+=[location]
                    priceListPage+=[price]

            self.locationList+=locationListPage
            self.priceList+=priceListPage
        except:
            pass

        self.nextUrl=response.xpath('//li[@class="next"]/a/@href').get()

        if self.nextUrl!=None:
            yield scrapy.Request(url=self.nextUrl,callback=self.parse)
        else:
            self.saveData()
        return


    def saveData(self):
        locationListOrdered=list(set(self.locationList))
        priceListOrdered=[ [] for i in range(len(locationListOrdered)) ]

        for location,price in zip(self.locationList,self.priceList):
            index=locationListOrdered.index(location)
            priceListOrdered[index]+=[price]
        if not(os.path.isdir(self.pathDB)): os.mkdir(self.pathDB)
        for location,priceListLocation in zip(locationListOrdered,priceListOrdered):
            hist=np.histogram(priceListLocation,bins=self.priceBins,range=(self.priceMin,self.priceMax))
            
            if os.path.isfile(os.path.join(self.pathDB,location+".txt")):
                f=open(os.path.join(self.pathDB,location+".txt"),"rb")
                data=(np.loadtxt(f,dtype=int))
                f.close()
            else:
                data=np.array([hist[1]])

            if self.date == data[-1][0]:
                data[-1][1:]=hist[0]
            else:
                data=np.append(data,[np.append(self.date,hist[0])],axis=0)
            f=open(os.path.join(self.pathDB,location+".txt"),"w+")
            np.savetxt(f,data,fmt="%d")
            f.close()
        return








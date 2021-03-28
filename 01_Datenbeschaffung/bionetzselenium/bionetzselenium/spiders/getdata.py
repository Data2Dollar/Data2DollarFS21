# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
# Zusaetzlich zu Scrapy importieren wir noch Selenium und die Systemtime
from selenium import webdriver
from time import sleep

# Dies ist unser normales von Scrapy angelegte Basistemplate 
class GetdataSpider(scrapy.Spider):
    name = 'getdata'
    allowed_domains = ['www.bionetz.ch']
    start_urls = ['http://www.bionetz.ch']

    def parse(self, response):
    	url = 'https://bionetz.ch/adressen/detailhandel/bio-fachgeschaefte.html'
    	# Hier integrieren wir den Webdriver
    	self.driver = webdriver.Chrome('C:\DRIVERS\chromedriver_win32\chromedriver.exe')
    	self.driver.get(url)
    	#Wir benoetigen eine while-Schleife, die ueberprueft, ob es noch eine naechste Seite gibt oder nicht
    	while self.driver.find_elements_by_xpath('//*[@title="Weiter"]'):
    		# Hier wird die Webseite im Selector gespeichert/uebergeben
    		sel = Selector(text=self.driver.page_source)
    		single_etikette = sel.xpath('//*[@class="listing-summary col-xs-12 col-sm-6"]')
    		for etikette in single_etikette:
    			unternehmens_name = etikette.xpath('.//*[@itemprop="name"]/text()').extract()
    			unternehmens_adresse = etikette.xpath('.//*[@class="address"]/text()').extract_first()
    			yield {'Name': unternehmens_name,
    				'Adresse': unternehmens_adresse}
    		# Da der "Naechste Seite" Button im Sichtfeld sein muss, scrollen wir auf der Webseite nach unten
    		element = self.driver.find_element_by_id('below-content')
    		self.driver.execute_script("arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-5);", element)
    		sel = Selector(text=self.driver.page_source)
    		sleep(3)
    		self.driver.find_element_by_xpath('//*[@title="Weiter"]').click()
    	# Am Ende schliessen wir den Webdriver
    	self.driver.close()

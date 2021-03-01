# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
 
import re
import csv
from time import sleep
 
class GetdataSpider(Spider):
    name = 'getdata'
   
    allowed_domains = ['blogabet.com']
    start_urls = ('https://blogabet.com',)
 
    def parse(self, response):
	        with open("urls.txt", "rt") as f:
	            start_urls = [url.strip() for url in f.readlines()]
	            for url in start_urls:
	                #sleep(20)
	                self.driver = webdriver.Chrome('C:\DRIVERS\chromedriver_win32\chromedriver.exe')
	                
	                #PROXY = "37.111.42.210:8080" # IP:PORT or HOST:PORT
	                #chrome_options = webdriver.ChromeOptions()
	                #chrome_options.add_argument('--proxy-server=%s' % PROXY)
	                #chrome = webdriver.Chrome(options=chrome_options) 

	                self.driver.get(url)
	                
	                try:
	                    self.driver.find_element_by_id('currentTab').click()
	                    sleep(3)
	                    self.logger.info('Sleeping for 5 sec.')
	                    self.driver.find_element_by_xpath('//*[@id="_blog-menu"]/div[2]/div/div[2]/a[3]').click()
	                    sleep(7)
	                    self.logger.info('Sleeping for 7 sec.')
	                except NoSuchElementException:
	                    self.logger.info('Blog does not exist anymore')

	                while True:                 
	                    try:
	                        element = self.driver.find_element_by_id('last_item')
	                        self.driver.execute_script("arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-5);", element)
	                        sleep(3)
	                        self.driver.find_element_by_id('last_item').click()
	                        sleep(7)
	                    

	                    except NoSuchElementException:
	                        self.logger.info('No more tipps')
	                        
	                        sel = Selector(text=self.driver.page_source)
	                        #paid_pics = post.xpath('.//div[@class="pins"]/h4[1]/span[@id="header-picks"]/text()').extract()

	                        allposts = sel.xpath('//*[@class="block media _feedPick feed-pick"]')
	  
	                        for post in allposts:
	                            username = post.xpath('.//div[@class="col-sm-7 col-lg-6 no-padding"]/a/@title').extract()
	                            publish_date = post.xpath('.//*[@class="bet-age text-muted"]/text()').extract()
	                            match = post.xpath('.//div[@class="col-xs-12 no-padding"]/h3/a/text()').extract()
	                            tipp = post.xpath('normalize-space(.//div[@class="pick-line"]/text())').extract()
	                            odd = post.xpath('.//span[@class="feed-odd"]/text()').extract()
	                            stack = post.xpath('.//span[@class="label label-default"]/text()').extract()

	                            # Extract WIN or LOSE of the Post
	                            lable = post.xpath('.//span[@class="enable-tooltip text-danger "]/@data-original-title').extract()
	                            if len(lable)>0:
	                                lable = post.xpath('.//span[@class="enable-tooltip text-danger "]/@data-original-title').extract()
	                            else:
	                                lable = 'WIN'
	                            # Extract the final result of the game
	                            result = post.xpath('.//div[@class="labels"]/span[4]/text()').extract()
	                            if len(result)>0:
	                                result = post.xpath('.//div[@class="labels"]/span[4]/text()').re('\s(.*)')
	                            else:
	                                result = post.xpath('.//div[@class="labels"]/span[3]/text()').re('\s(.*)')

	                            sport = post.xpath('.//small[@class="text-muted"]/span[@class="hidden-xs"][1]/text()').re('^\S*')
	                            country = post.xpath('normalize-space(substring-before(.//small[@class="text-muted"]/span[@class="hidden-xs"]/following-sibling::text(),"/"))').extract()
	            
	                            analysis = post.xpath('.//div[@class="feed-pick-title"]/div[@class="col-xs-12 _text-more  feed-analysis"]/div[contains(@id,"feed_pick_analysis")]/p/text()').extract()
	                            if len(analysis)>0:
	                                analysis = post.xpath('.//div[@class="feed-pick-title"]/div[@class="col-xs-12 _text-more  feed-analysis"]/div[contains(@id,"feed_pick_analysis")]/p/text()').extract()
	                            else:
	                                analysis = 'No content posted'
	       

	                            #kickoff = post.xpath('.//small[@class="text-muted"]/span[@class="hidden-xs"]/following-sibling::text()').re('([^/]+$)')
	                            #kickoff = [x.strip(' ') for x in kickoff]
	                            #kickoff = [kickoff[1]]
	                            kickoff = post.xpath('.//small[@class="text-muted"]/span[@class="hidden-xs"][2]/following-sibling::text()').re('([^/]+$)')                           

	                            yield {'Username': username,
	                                'Publish date': publish_date,
	                                'Match': match,
	                                'Tipp': tipp,
	                                'Odd': odd,
	                                'Stack': stack,
	                                'Lable': lable,
	                                'Result': result,
	                                'Sport': sport,
	                                'Country': country,
	                                'Kickoff Date': kickoff,
	                                'Post Content': analysis}
	                        self.driver.close()
	                        break
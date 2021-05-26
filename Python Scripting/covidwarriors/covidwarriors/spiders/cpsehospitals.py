# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest


class CovidwarriorsSpider(scrapy.Spider):
    name = 'cpsehospitals'
    start_urls = ['https://covidwarriors.gov.in/covid_cpse_hospitals.aspx']

    def parse(self, response):
        data = response.css('#tblExportMain > tbody')
        for each in data[1:]:
            raw = each.css('td')
            item = dict()
            item['cpse_name'] = raw[1].css('::text').get().strip()
            item['state_name'] = raw[2].css('::text').get().strip()
            item['hospital_name'] = raw[3].css('<br>').css('::text').getall()
            item['status'] = raw[3].css('::text').getall()[5].strip()
            item['address'] = raw[3].css('::text').getall()[8].strip()
            #if raw[3].css('::text').getall()[11].strip() == 'Email Id : ':
                #item['phone_no']= ''
                #css('::text').extract_first().strip()
                #item['email_id'] = raw[3].css('::text').getall()[13].strip()
            #elif raw[3].css('::text').getall()[11].strip() == 'Email Id : ':
                #item['phone_no'] = raw[3].css('::text').getall()[11].strip()
                #item['email_id'] = raw[3].css('::text').getall()[14].strip()
            print (item)
            #//*[@id="tblExportMain"]/tbody[50]/tr/td[4]/text()[4]
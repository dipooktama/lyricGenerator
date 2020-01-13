# -*- coding: utf-8 -*-
import scrapy


class LyricscraperSpider(scrapy.Spider):
    name = 'lyricscraper'
    allowed_domains = ['lirik.kapanlagi.com']
    start_urls = ['http://lirik.kapanlagi.com/']

    def parse(self, response):
        pass

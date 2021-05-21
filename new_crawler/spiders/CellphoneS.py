import scrapy
from scrapy import item
from new_crawler.items import productItems
from new_crawler.items import schemaItems
from new_crawler.matching import *

class MacbookCellphonesSpider(scrapy.Spider):
    name = 'macbook_cellphoneS'
    allowed_domains = ['cellphones.com.vn']
    start_urls = ['https://cellphones.com.vn/laptop/mac.html',
                  'https://cellphones.com.vn/laptop/mac.html?p=2']
    handle_httpstatus_list = [301]


    def parse(self, response):
        # Request tới từng sản phẩm có trong danh sách các Macbook dựa vào href
        for product in response.css(".list-laptop > ul > li"):
            # item = DemoScrapyItem()
            # item['product_name'] = product.css('div > a > h3 ::text').extract()[0]  # Tên macbook
            # #item['product_name'] = "XXXXXX"
            # item['price_sale'] = product.css('.price-box > p.special-price > span::text').extract_first()

            # item['price'] = product.css('.price-box > p.old-price > span::text').extract_first()

            # item['rate_average'] = 'abc'
            if(len(product.css(".lt-product-group-cau-hinh > table > tr > td"))):
                cpu = product.css(".lt-product-group-cau-hinh > table > tr > td ")[1].css("::text").extract_first()
                vga = product.css(".lt-product-group-cau-hinh > table > tr > td ")[3].css("::text").extract_first()
                dr = product.css(".lt-product-group-cau-hinh > table > tr > td ")[5].css("::text").extract_first()
            else:
                cpu = ""
                vga = ""
                dr = ""
            item_url = product.css(".lt-product-group-info > a ::attr(href)").extract_first()
            yield scrapy.Request(response.urljoin(item_url), callback=self.parse_macbook, cb_kwargs={'cpu': cpu, 'vga': vga, 'dr': dr, "url":item_url})

    def parse_macbook(self, response, cpu,vga, dr, url):
        yield convert( {
            'name': response.css(
                'div.topview > h1 ::text').extract_first(),
            'price_sale': response.css(
                'p.special-price > span::text').extract_first(),
            'price': response.css(
                'p.old-price > span::text').extract_first(),
            'rate': response.css(
                'p.averageRatings::text').extract_first(),
            'cpu': cpu,
            'gpu': vga,
            'storage': dr,
            'url' : url,
            'website': self.allowed_domains[0]
        })





    # def parse(self, response):
    #     # Request tới từng sản phẩm có trong danh sách các Macbook dựa vào href
    #     for item_url in response.css(".list-laptop>ul >li > div > a ::attr(href)").getall():
    #         yield scrapy.Request(response.urljoin(item_url), callback=self.parse_macbook) # Nếu có sản phẩm thì sẽ gọi tới function parse_macbook
        
    #    # nếu có sản phẩm kế tiếp thì tiếp tục crawl
    #     next_page = response.css("li.next > a ::attr(href)").extract_first()
    #     if next_page:
    #         yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
    
    # def parse_macbook(self, response):
    #     item = DemoScrapyItem()
        
    #     item['product_name'] = response.css(
    #         'div.topview > h1 ::text').extract_first() # Tên macbook
        
    #     # out_of_stock = response.css('span.productstatus ::text').extract_first() # Tình trạng còn hàng hay không
    #     # if out_of_stock: 
    #     #     item['price'] = response.css(
    #     #     'strong.pricesell ::text').extract_first()
    #     # else: 
    #     #     item['price'] = response.css(
    #     #     'aside.price_sale > div.area_price.notapply > strong ::text').extract_first()
    #     item['price_sale'] = response.css('p.special-price > span::text').extract_first()
        
    #     item['price'] = response.css('p.old-price > span::text').extract_first()
    #     # discount_online = response.css('div.box-online.notapply').extract_first() # Check nếu có giảm giá khi mua online hay không
    #     # if discount_online:
    #     #     item['price_sale'] = response.css(
    #     #         'aside.price_sale > div.box-online.notapply > div > strong ::text').extract_first()
    #     # else:
    #     #     item['price_sale'] = response.css(
    #     #         'span.hisprice ::text').extract_first()
                
    #     item['rate_average'] = response.css('p.averageRatings::text').extract_first()
    #     yield item

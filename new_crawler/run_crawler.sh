#!/bin/bash

echo "Start crawling"
scrapy crawl macbook_cellphoneS -o macbook.json
scrapy crawl hanoicom -o macbook.json
scrapy crawl mac24h -o macbook.json
scrapy crawl macone -o macbook.json
scrapy crawl MacbookStore -o macbook.json
scrapy crawl techone -o macbook.json
scrapy crawl TheGioiDiDong_iphone -o macbook.json
scrapy crawl apple_watch_tgdd -o macbook.json
scrapy crawl xtmobile_iphone -o macbook.json
scrapy crawl click_buy_iphone -o macbook.json
scrapy crawl click_buy_apple_watch -o macbook.json
scrapy crawl cell_phone_iphone -o macbook.json
scrapy crawl dienthoaimoi_iphone -o macbook.json
scrapy crawl dienthoaimoi_applewatch -o macbook.json
scrapy crawl dien_may_xanh_iphone -o macbook.json
scrapy crawl onewaymobile_watch -o macbook.json
scrapy crawl onewaymobile_iphone -o macbook.json
scrapy crawl nguyenkim_watch -o macbook.json
scrapy crawl nguyenkim_iphone -o macbook.json
scrapy crawl truesmart_iphone -o macbook.json
scrapy crawl iphone_24hstore -o macbook.json
scrapy crawl watch_24hstore -o macbook.json
scrapy crawl xtsmart_iphone -o macbook.json
scrapy crawl didongthongminh_iphone -o macbook.json
echo "Finish crawl!"

echo "Transforming"
PYTHONPATH=$PWD python data_filling.py
echo "Finish transform!"

echo "Pushing to elasticSearch"
PYTHONPATH=$PWD python csv_to_elastic.py
echo "Finish push!"
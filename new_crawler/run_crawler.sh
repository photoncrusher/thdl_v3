#!/bin/bash

echo "Start crawling"
scrapy crawl macbook_cellphoneS -o product.json
scrapy crawl hanoicom -o product.json
scrapy crawl mac24h -o product.jsonn
scrapy crawl macone -o product.json
scrapy crawl MacbookStore -o product.json
scrapy crawl techone -o product.json
scrapy crawl TheGioiDiDong_iphone -o product.json
scrapy crawl apple_watch_tgdd -o product.json
scrapy crawl xtmobile_iphone -o product.json
scrapy crawl click_buy_iphone -o product.json
scrapy crawl click_buy_apple_watch -o product.json
scrapy crawl cell_phone_iphone -o product.json
scrapy crawl dienthoaimoi_iphone -o product.json
scrapy crawl dienthoaimoi_applewatch -o product.json
scrapy crawl dien_may_xanh_iphone -o product.json
scrapy crawl onewaymobile_watch -o product.json
scrapy crawl onewaymobile_iphone -o product.json
scrapy crawl nguyenkim_watch -o product.json
scrapy crawl nguyenkim_iphone -o product.json
scrapy crawl truesmart_iphone -o product.json
scrapy crawl iphone_24hstore -o product.json
scrapy crawl watch_24hstore -o product.json
scrapy crawl xtsmart_iphone -o product.json
scrapy crawl didongthongminh_iphone -o product.json
echo "Finish crawl!"

echo "Transforming"
PYTHONPATH=$PWD json_csv.py
echo "Finish transform!"

echo "Transforming"
PYTHONPATH=$PWD python data_filling.py
echo "Finish transform!"

echo "Pushing to elasticSearch"
PYTHONPATH=$PWD python csv_to_elastic.py
echo "Finish push!"
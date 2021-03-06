import scrapy
from scrapy_splash import SplashRequest
from scrapy import *
import requests
from bs4 import BeautifulSoup
from new_crawler.items import productItems
from new_crawler.items import schemaItems
from new_crawler.matching import *

class TheGioiDiDong_iphone(scrapy.Spider):
    name = 'TheGioiDiDong_iphone'
    # allowed_domains = ["thegioididong.com"]
    start_urls = ["https://www.thegioididong.com/dtdd-apple-iphone"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(1))
                assert(splash:runjs('document.getElementsByClassName("viewmore")[0].click();'))
                assert(splash:wait(1))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)
            # yield SplashRequest(
            #     url,
            #     endpoint="render.html",
            #     callback=self.parse,
            #     headers=headers,
            #     meta={
            #         "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
            #     },
            # )

    def parse(self, response):
        items = response.css('li.item')
        for item in items:
            Ram = ''
            CPU = ''
            kich_thuoc_man_hinh = ''
            ROM = ''
            do_phan_giai_man_hinh = ''
            Pin = ''
            Camera_sau = ''
            Camera_truoc = ''
            bluetooth = ''
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            link = 'https://www.thegioididong.com/' + str(item.css('a').attrib['href'])
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            informations = soup.find('ul', class_='parameter')
            try:
                man_hinh = informations.find('li', class_='g6459_79_77')
                kich_thuoc_man_hinh = man_hinh.split(',')[1]
            except:
                print()
            try:
                Ram = informations.find('li', class_='g50').find('div').text
            except:
                print()
            try:
                ROM = informations.find('li', class_='g49').find('div').text
            except:
                print()
            try:
                Camera_sau = informations.find('li', class_='g27').find('div').text
            except:
                print()
            try:
                Camera_truoc = informations.find('li', class_='g29').find('div').text
            except:
                print()
            try:
                Pin = informations.find('li', class_='g84_26846').find('div').text
            except:
                print()
            try:
                CPU = informations.find('li', class_='g6059').find('div').text
            except:
                print()

            yield convert( {
                'T??n s???n ph???m': str(item.css('h3::text').get()).replace('\n', ''),
                'Gi?? s???n ph???m': str(item.css('div.price strong::text').get()).replace('???', ' VN??'),
                'K??ch th?????c m??n h??nh': kich_thuoc_man_hinh,
                'Ram': Ram,
                'B??? nh??? trong': ROM,
                'CPU': CPU,
                'Camera sau': Camera_sau,
                'Camera tr?????c': Camera_truoc,
                'Pin': Pin,
                '????? ph??n gi???i m??n h??nh': do_phan_giai_man_hinh,
                'Bluetooth': bluetooth,
                'Link': link,
                'Lo???i s???n ph???m': 'IPHONE',
                'T??n c???a h??ng': 'THE GIOI DI DONG'
            }
            )

class TheGioiDiDong_watch(scrapy.Spider):
    name = 'apple_watch_tgdd'
    # allowed_domains = ["thegioididong.com"]
    start_urls = ["https://www.thegioididong.com/dong-ho-thong-minh-apple"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(1))
                assert(splash:runjs('try{document.getElementsByClassName("viewmore")[0].click();}catch(e){}'))
                assert(splash:wait(2))
                assert(splash:runjs('try{document.getElementsByClassName("viewmore")[0].click();}catch(e){}'))
                assert(splash:wait(2))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                endpoint="render.html",
                callback=self.parse,
                headers=headers,
                meta={
                    "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
                },
            )

    def parse(self, response):
        items = response.css('li.item')
        for item in items:
            loai_man_hinh = ''
            chip = ''
            tinh_nang_khac = ''
            pin = ''
            bluetooth = ''
            ho_tro_sim = ''
            link = 'https://www.thegioididong.com/' + item.css('a').attrib['href']
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            informations = soup.find('ul', class_='parameter')
            try:
                loai_man_hinh = informations.find('li', class_='g16521_16522').find('div').text
            except:
                print()
            try:
                pin = informations.find('li', class_='g16531').find('div').text
            except:
                print()
            try:
                tinh_nang_khac = informations.find('li', class_='g16534').find('div').text
            except:
                print()

            yield convert({
                'T??n s???n ph???m': str(item.css('h3::text').get()).replace('\n', ''),
                'Gi?? s???n ph???m': str(item.css('strong.price::text').get()).replace('???', ' VN??'),
                'Lo???i m??n h??nh': loai_man_hinh,
                'Pin': pin,
                'T??nh n??ng': tinh_nang_khac,
                'H??? tr??? sim': ho_tro_sim,
                'Chip': chip,
                'Bluetooth': bluetooth,
                'Link': link,
                'Lo???i s???n ph???m': 'APPLE WATCH',
                'C???a h??ng': 'THE GIOI DI DONG'
            })


class xtmobile_iphone(scrapy.Spider):
    name = 'xtmobile_iphone'
    # allowed_domains = ["thegioididong.com"]
    start_urls = ["https://www.xtmobile.vn/apple"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(1))
                assert(splash:runjs('try{document.getElementsByClassName("pagination-more")[0].getElementsByClassName("fa fa-caret-down")[0].click();}catch(e){}'))
                assert(splash:wait(2))
                assert(splash:runjs('try{document.getElementsByClassName("pagination-more")[0].getElementsByClassName("fa fa-caret-down")[0].click();}catch(e){}'))
                assert(splash:wait(2))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                endpoint="render.html",
                callback=self.parse,
                headers=headers,
                meta={
                    "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
                },
            )

    def parse(self, response):
        items = response.css('div.product-base-grid')
        for item in items:
            price = item.css('div.price::text').get()
            price = price[0:len(price) - 1] + ' VN??'
            link = 'https://www.xtmobile.vn' + item.css('h3')[0].css('a').attrib['href']
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            colors = soup.find('ul', class_='color-list-show').find_all('li')
            mau = ''
            for c in colors:
                mau += c.find('p').text + ' '

            thongtin = soup.find('ul', class_='parametdesc').find_all('strong')

            yield convert({
                'T??n s???n ph???m': item.css('h3 a::text')[0].get(),
                'Gi?? s???n ph???m': price,
                'M??u': mau,
                'M??n h??nh': thongtin[0].text,
                'Camera tr?????c': thongtin[1].text,
                'Camera sau': thongtin[2].text,
                'Chip': thongtin[3].text,
                'Ram': thongtin[4].text,
                'B??? nh??? trong': thongtin[5].text,
                'Th??? sim': thongtin[6].text,
                'Pin': thongtin[7].text,
                'H??? ??i???u h??nh': thongtin[8].text,
                'Link': link,
                'Lo???i s???n ph???m': 'IPHONE',
                'C???a h??ng': 'XTMOBILE'
            })


class Clickbuy_iphone(scrapy.Spider):
    name = 'click_buy_iphone'
    start_urls = ["https://hcm.clickbuy.com.vn/danh-muc/iphone/"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(1))
                assert(splash:runjs('for(var i = 0 ; i < 10 ; i ++){document.getElementById("sb-infinite-scroll-load-more-1").getElementsByTagName("a")[0].click();}'))
                assert(splash:wait(5))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                headers=headers,
                meta={
                    "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
                },
            )

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

        items = response.xpath('//*[@id="main"]/ul').css('li.col-6')
        for item in items:
            link = item.css('a').attrib['href']
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")

            try:
                price = str(soup.find('p', class_='price').find('span').text)
                price = price.replace('\xa0???', ' VN??')
            except:
                price = None
            try:
                color = soup.find('tr',
                                  class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_mau-sac').find(
                    'p').text
            except:
                color = None
            try:
                memory = soup.find('tr',
                                   class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_bo-nho-trong').find(
                    'p').text
            except:
                memory = None
            try:
                camera_chinh = soup.find('tr',
                                         class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_camera-chinh').find(
                    'p').text
            except:
                camera_chinh = None
            try:
                camera_phu = soup.find('tr',
                                       class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_camera-phu').find(
                    'p').text
            except:
                camera_phu = None
            try:
                CPU = soup.find('tr',
                                class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_cpu').find(
                    'p').text
            except:
                CPU = None
            try:
                dophangiai = soup.find('tr',
                                       class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_do-phan-giai-man-hinh').find(
                    'p').text
            except:
                dophangiai = None
            try:
                pin = soup.find('tr',
                                class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_dung-luong-pin').find(
                    'p').text
            except:
                pin = None
            try:
                hedieuhanh = soup.find('tr',
                                       class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_he-dieu-hanh').find(
                    'p').text
            except:
                hedieuhanh = None
            try:
                kichthuocmanhinh = soup.find('tr',
                                             class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_kich-thuoc-man-hinh').find(
                    'p').text
            except:
                kichthuocmanhinh = None
            try:
                ram = soup.find('tr',
                                class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_ram').find(
                    'p').text
            except:
                ram = None
            yield convert({
                'T??n s???n ph???m': item.css('h2.woocommerce-loop-product__title::text').get(),
                'Gi?? s???n ph???m': price,
                'Link': link,
                # 'M??u s???c': color,
                'B??? nh??? trong': memory,
                'Camera ch??nh': camera_chinh,
                'Camera ph???': camera_phu,
                'CPU': CPU,
                "????? ph??n gi???i m??n h??nh": dophangiai,
                'Pin': pin,
                # 'H??? ??i???u h??nh': hedieuhanh,
                'K??ch th?????c m??n h??nh': kichthuocmanhinh,
                'Bluetooth': '',
                'Ram': ram,
                'Lo???i s???n ph???m': 'IPHONE',
                'C???a h??ng': 'CLICK_BUY'
            })


class Clickbuy_Apple_Watch(scrapy.Spider):
    name = 'click_buy_apple_watch'
    start_urls = ["https://hcm.clickbuy.com.vn/danh-muc/applewatch/"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(1))
                assert(splash:runjs('for(var i = 0 ; i < 10 ; i ++){document.getElementById("sb-infinite-scroll-load-more-1").getElementsByTagName("a")[0].click();}'))
                assert(splash:wait(5))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                headers=headers,
                meta={
                    "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
                },
            )

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

        items = response.xpath('//*[@id="main"]/ul').css('li.col-6')
        for item in items:
            link = item.css('a').attrib['href']
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            chip = ''
            pin = ''
            man_hinh = ''
            try:
                price = str(soup.find('p', class_='price').find('span').text)
                price = price.replace('\xa0???', '')
            except:
                price = None
            try:
                chip = soup.find('tr',
                                 class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_cpu').find(
                    'p').text
            except:
                chip = None
            try:
                pin = soup.find('tr',
                                class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_thoi-gian-dung').find(
                    'p').text
            except:
                pin = None
            try:
                kich_thuoc = soup.find('tr',
                                       class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_kich-thuoc-man-hinh').find(
                    'p').text
            except:
                kich_thuoc = None
            try:
                do_phan_giai = soup.find('tr',
                                         class_='woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_do-phan-giai-man-hinh').find(
                    'p').text
            except:
                do_phan_giai = None

            man_hinh = kich_thuoc + ', ' + do_phan_giai

            yield convert({
                'T??n s???n ph???m': item.css('h2.woocommerce-loop-product__title::text').get(),
                'Gi?? s???n ph???m': price,
                'Chip': chip,
                'Pin': pin,
                'M??n h??nh': man_hinh,
                'T??nh n??ng': None,
                'Bluetooth': None,
                'H??? tr??? sim': None,
                'Link': link,
                'Lo???i s???n ph???m': 'APPLE WATCH',
                'C???a h??ng': 'CLICK_BUY'
            })


class Cell_phone_iphone(scrapy.Spider):
    name = 'cell_phone_iphone'
    start_urls = ["https://cellphones.com.vn/mobile/apple.html"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(1))
                assert(splash:runjs('document.getElementsByClassName("pagination")[1].getElementsByTagName("a")[0].click();'))
                assert(splash:wait(5))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                headers=headers,
            )

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        items = response.css('li.cate-pro-short')
        for item in items:
            price = str(item.css('span.price::text').get())
            link = item.css('div.lt-product-group-info')[0].css('a').attrib['href']
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            thongtin = soup.find('div', class_='content')
            try:
                bluetooth = thongtin.find_all('tr')[29].find_all('td')[1].text
            except:
                print()

            yield convert({
                "T??n s???n ph???m": str(item.css('div.lt-product-group-info')[0].css('h3::text').get()).replace('\t', ''),
                "Link": link,
                "Gi?? s???n ph???m": price.replace('\xa0???', ' VN??'),
                "K??ch th?????c m??n h??nh": thongtin.find_all('tr')[0].find_all('td')[1].text,
                "????? ph??n gi???i m??n h??nh": thongtin.find_all('tr')[1].find_all('td')[1].text,
                "Camera sau": thongtin.find_all('tr')[2].find_all('td')[1].text,
                "Camera tr?????c": thongtin.find_all('tr')[3].find_all('td')[1].text,
                "CPU": thongtin.find_all('tr')[4].find_all('td')[1].text,
                "Ram": thongtin.find_all('tr')[5].find_all('td')[1].text,
                "B??? nh??? trong": thongtin.find_all('tr')[6].find_all('td')[1].text,
                "Pin": thongtin.find_all('tr')[7].find_all('td')[1].text,
                "Bluetooth": bluetooth,
                'Lo???i s???n ph???m': 'IPHONE',
                'C???a h??ng': 'CELL_PHONE'
            })
        if str(response.css('ul.pagination')[1].css('a::text').get()) == 'Ti???p ':
            yield SplashRequest(
                response.url,
                callback=self.parse,
                headers=headers,
                meta={
                    "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
                },
            )


class dienthoaimoi_iphone(scrapy.Spider):
    name = 'dienthoaimoi_iphone'
    start_urls = ["https://dienthoaimoi.vn/dien-thoai-apple-iphone-pcm135.html"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(2))
                assert(splash:runjs('document.getElementsByClassName("next-page")[0].click();'))
                assert(splash:wait(5))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                headers=headers,
            )

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        items = response.css('div.product_grid')[0].css('div.item')
        for item in items:
            price = item.css('div.price_current::text').get()
            link = item.css('a.name').attrib['href']
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            thongtins = soup.find('table', class_='charactestic_table').find_all('tr')
            pin = ''
            for thongtin in thongtins:
                if str(thongtin.find_all('td')[0].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                    '') == 'C??ng ngh??? m??n h??nh':
                    Cong_nghe_man_hinh = str(thongtin.find_all('td')[1].text).replace('\t', '').replace('\n',
                                                                                                        '').replace(
                        '\r', '')
                elif str(thongtin.find_all('td')[0].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                      '') == '????? ph??n gi???i':
                    Do_phan_giai = str(thongtin.find_all('td')[1].text).replace('\t', '').replace('\n', '').replace(
                        '\r', '')
                elif str(thongtin.find_all('td')[0].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                      '') == 'M??n h??nh r???ng':
                    Kich_thuoc_man_hinh = str(thongtin.find_all('td')[1].text).replace('\t', '').replace('\n',
                                                                                                         '').replace(
                        '\r', '')
                elif str(thongtin.find_all('td')[0].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                      '') == 'Camera sau':
                    Camera_sau = str(thongtin.find_all('td')[1].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                                  '')
                elif str(thongtin.find_all('td')[0].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                      '') == 'Camera tr?????c':
                    Camera_truoc = str(thongtin.find_all('td')[1].text).replace('\t', '').replace('\n', '').replace(
                        '\r', '')
                elif str(thongtin.find_all('td')[0].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                      '') == 'Camera tr?????c':
                    Camera_truoc = str(thongtin.find_all('td')[1].text).replace('\t', '').replace('\n', '').replace(
                        '\r', '')
                elif str(thongtin.find_all('td')[0].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                      '') == '????n Flash':
                    flash = str(thongtin.find_all('td')[1].text).replace('\t', '').replace('\n', '').replace('\r', '')
                elif str(thongtin.find_all('td')[0].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                      '') == 'H??? ??i???u h??nh':
                    he_dieu_hanh = str(thongtin.find_all('td')[1].text).replace('\t', '').replace('\n', '').replace(
                        '\r', '')
                elif str(thongtin.find_all('td')[0].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                      '') == 'Dung l?????ng pin':
                    pin = str(thongtin.find_all('td')[1].text).replace('\t', '').replace('\n', '').replace('\r', '')
            yield convert({
                "T??n s???n ph???m": str(item.css('h2 a::text').get()).replace('\n', '').replace('\t', ''),
                "Gi?? s???n ph???m": price.replace('???', ' VN??'),
                "C??ng ngh??? m??n h??nh": Cong_nghe_man_hinh,
                "????? ph??n gi???i": Do_phan_giai,
                "K??ch th?????c m??n h??nh": Kich_thuoc_man_hinh,
                "Camera sau": Camera_sau,
                "Camera tr?????c": Camera_truoc,
                "????n flash": flash,
                "Pin": (pin == '' and None or pin),
                "H??? ??i???u h??nh": he_dieu_hanh,
                "Link": link,
                'Lo???i s???n ph???m': 'IPHONE',
                'C???a h??ng': 'DIEN THOAI MOI'
            })

        yield SplashRequest(
            response.url,
            callback=self.parse,
            headers=headers,
            meta={
                "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
            },
        )


class dienthoaimoi_applewatch(scrapy.Spider):
    name = 'dienthoaimoi_applewatch'
    start_urls = ["https://dienthoaimoi.vn/dong-ho-apple-watch-pc298.html"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(2))
                assert(splash:runjs('document.getElementsByClassName("next-page")[0].click();'))
                assert(splash:wait(5))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                headers=headers,
            )

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        items = response.css('div.product_grid')[0].css('div.item')
        for item in items:
            price = item.css('div.price_current::text').get()
            link = item.css('a.name').attrib['href']
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            thongtins = soup.find('table', class_='charactestic_table').find_all('tr')
            man_hinh = ''
            kich_thuoc_man_hinh = ''
            thoi_gian_su_dung = ''
            CPU = ''
            He_dieu_hanh = ''
            ngon_ngu = ''
            for thongtin in thongtins:
                if str(thongtin.find_all('td')[0].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                    '') == 'M??n h??nh':
                    man_hinh = str(thongtin.find_all('td')[1].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                                '')
                elif str(thongtin.find_all('td')[0].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                      '') == 'K??ch th?????c m??n h??nh':
                    kich_thuoc_man_hinh = str(thongtin.find_all('td')[1].text).replace('\t', '').replace('\n',
                                                                                                         '').replace(
                        '\r', '')
                elif str(thongtin.find_all('td')[0].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                      '') == 'Th???i gian s??? d???ng':
                    thoi_gian_su_dung = str(thongtin.find_all('td')[1].text).replace('\t', '').replace('\n',
                                                                                                       '').replace('\r',
                                                                                                                   '')
                elif str(thongtin.find_all('td')[0].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                      '') == 'H??? ??i???u h??nh':
                    He_dieu_hanh = str(thongtin.find_all('td')[1].text).replace('\t', '').replace('\n', '').replace(
                        '\r', '')
                elif str(thongtin.find_all('td')[0].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                      '') == 'Ng??n ng???':
                    ngon_ngu = str(thongtin.find_all('td')[1].text).replace('\t', '').replace('\n', '').replace('\r',
                                                                                                                '')

            yield convert({
                "T??n s???n ph???m": str(item.css('h2 a::text').get()).replace('\n', '').replace('\t', ''),
                "Gi?? s???n ph???m": price.replace('???', ' VN??'),
                "m??n h??nh": (man_hinh == '' and None or man_hinh),
                "K??ch th?????c m??n h??nh": (kich_thuoc_man_hinh == '' and None or kich_thuoc_man_hinh),
                "Th???i gian s??? d???ng": (thoi_gian_su_dung == '' and None or thoi_gian_su_dung),
                'H??? ??i???u h??nh': (He_dieu_hanh == '' and None or He_dieu_hanh),
                "Ng??n ng???": (ngon_ngu == '' and None or ngon_ngu),
                "Link": link,
                "Th??? lo???i s???n ph???m": 'APPLE WATCH',
                "C???a h??ng": 'DIEN THOAI MOI'
            })

        yield SplashRequest(
            response.url,
            callback=self.parse,
            headers=headers,
            meta={
                "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
            },
        )


class dien_may_xanh_iphone(scrapy.Spider):
    name = 'dien_may_xanh_iphone'
    start_urls = ["https://www.dienmayxanh.com/dien-thoai-apple-iphone"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(2))
                assert(splash:runjs('document.getElementsByClassName("loadmore")[0].click();'))
                assert(splash:wait(5))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                headers=headers,
                meta={
                    "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
                },
            )

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        items = response.css('div.prdWrFixHe')
        print(len(items))
        for item in items:
            thongtins = item.css('div.prdTooltip')[0]
            yield convert({
                "T??n s???n ph???m": item.css('div.prdName span::text').get(),
                "Gi?? s???n ph???m": str(item.css('strong.prPrice::text').get()).replace('???', ' VN??'),
                "M??n h??nh": str(thongtins.css('span::text')[0].get()).split(', ')[0].replace('"', ' inch'),
                "Chip": str(thongtins.css('span::text')[0].get()).split(', ')[1],
                'RAM': str(thongtins.css('span::text')[1].get()).split(', ')[0].replace('RAM ', ''),
                'B??? nh??? trong': str(thongtins.css('span::text')[1].get()).split(', ')[1].replace('ROM ', ''),
                'Camera sau': str(thongtins.css('span::text')[2].get()).replace('Camera sau: ', ''),
                'Camera tr?????c': str(thongtins.css('span::text')[3].get()).replace('Camera tr?????c:  ', ''),
                'Pin': str(thongtins.css('span::text')[4].get()).split(', ')[0].replace('Pin ', ''),
                'S???c': str(thongtins.css('span::text')[4].get()).split(', ')[1].replace('S???c ', ''),
                'Lo???i s???n ph???m': 'IPHONE',
                'C???a h??ng': 'DIEN MAY XANH'
            })

class onewaymobile_watch(scrapy.Spider):
    name = 'onewaymobile_watch'
    start_urls = ["https://onewaymobile.vn/apple-watch-pc61.html"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(2))
                assert(splash:runjs('document.getElementsByClassName("next-page")[0].getElementsByTagName("i")[0].click();'))
                assert(splash:wait(5))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                headers=headers,
            )

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'}
        items = response.xpath('//*[@id="home-product-list"]/div').css('div.image-check')
        for item in items:
            link = item.css('div.title-product')[0].css('a').attrib['href']
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            loai_man_hinh = ''
            chip = ''
            tinh_nang_khac = ''
            pin = ''
            bluetooth = ''
            ho_tro_sim = ''
            try:
                informations = soup.find_all('table', class_='shop_attributes')[1].find_all('tr')
                for information in informations:
                    if information.find('th').text == 'Lo???i m??n h??nh' or information.find('th').text == 'Ki???u m??n h??nh':
                        loai_man_hinh = information.find('p').text
                    elif information.find('th').text == 'Chipset' or information.find('th').text == 'Chip x??? l?? (CPU)':
                        chip = information.find('p').text
                    elif information.find('th').text == 'T??nh n??ng kh??c':
                        tinh_nang_khac = information.find('p').text
                    elif information.find('th').text == 'Dung l?????ng pin (mAh)' or information.find('th').text == 'Pin':
                        pin = information.find('p').text
                    elif information.find('th').text == 'Bluetooth':
                        bluetooth = information.find('p').text
                    elif information.find('th').text == 'H??? tr??? nhi???u sim':
                        ho_tro_sim = information.find('p').text
            except:
                print("error: " + str(link))

            yield convert({
                "T??n s???n ph???m": item.css('div.title-product')[0].css('a::text').get(),
                "Gi?? s???n ph???m": str(item.css('span.final-price::text').get()).replace('??', ' VN??'),
                "Lo???i m??n h??nh": loai_man_hinh,
                "Chip": chip,
                "T??nh n??ng kh??c": tinh_nang_khac,
                "Pin": pin,
                "Bluetooth": bluetooth,
                "H??? tr??? sim": ho_tro_sim,
                "Link": link,
                'Th??? lo???i s???n ph???m': 'APPLE WATCH',
                'C???a h??ng': 'ONE WAY MOBILE'
            })

        yield SplashRequest(
            response.url,
            callback=self.parse,
            headers=headers,
            meta={
                "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
            },
        )


class onewaymobile_iphone(scrapy.Spider):
    name = 'onewaymobile_iphone'
    start_urls = ["https://onewaymobile.vn/iphone-pc29.html"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(2))
                assert(splash:runjs('document.getElementsByClassName("next-page")[0].getElementsByTagName("i")[0].click();'))
                assert(splash:wait(5))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                headers=headers,
            )

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'}
        items = response.xpath('//*[@id="home-product-list"]/div').css('div.image-check')
        for item in items:
            link = item.css('div.title-product')[0].css('a').attrib['href']
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            Ram = ''
            CPU = ''
            kich_thuoc_man_hinh = ''
            ROM = ''
            do_phan_giai_man_hinh = ''
            Pin = ''
            Camera_sau = ''
            Camera_truoc = ''
            bluetooth = ''
            try:
                informations = soup.find_all('table', class_='shop_attributes')[1].find_all('tr')
                for information in informations:
                    if information.find('th').text == 'RAM':
                        Ram = information.find('p').text
                    elif information.find('th').text == 'CPU' or information.find('th').text == 'Chip x??? l?? (CPU)':
                        CPU = information.find('p').text
                    elif information.find('th').text == 'K??ch th?????c m??n h??nh':
                        kich_thuoc_man_hinh = information.find('p').text
                    elif information.find('th').text == 'B??? nh??? trong':
                        ROM = information.find('p').text
                    elif information.find('th').text == 'Bluetooth':
                        bluetooth = information.find('p').text
                    elif information.find('th').text == '????? ph??n gi???i m??n h??nh':
                        do_phan_giai_man_hinh = information.find('p').text
                    elif information.find('th').text == 'Pin' or information.find('th').text == 'Dung l?????ng pin (mAh)':
                        Pin = information.find('p').text
                    elif information.find('th').text == 'M??y ???nh ch??nh':
                        Camera_sau = information.find('p').text
                    elif information.find('th').text == 'M??y ???nh ph???':
                        Camera_truoc = information.find('p').text
            except:
                print("error: " + str(link))

            yield convert({
                "T??n s???n ph???m": item.css('div.title-product')[0].css('a::text').get(),
                "Gi?? s???n ph???m": str(item.css('span.final-price::text').get()).replace('??', ' VN??'),
                "K??ch th?????c m??n h??nh ": kich_thuoc_man_hinh,
                "????? ph??n gi???i m??n h??nh": do_phan_giai_man_hinh,
                "CPU": CPU,
                "RAM": Ram,
                "B??? nh??? trong": ROM,
                "Pin": Pin,
                "Bluetooth": bluetooth,
                "Camera sau": Camera_sau,
                "Camera tr?????c": Camera_truoc,
                "Link": link,
                'Th??? lo???i s???n ph???m': 'IPHONE',
                'C???a h??ng': 'ONE WAY MOBILE'
            })

        yield SplashRequest(
            response.url,
            callback=self.parse,
            headers=headers,
            meta={
                "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
            },
        )


class nguyenkim_watch(scrapy.Spider):
    name = 'nguyenkim_watch'
    start_urls = ["https://www.nguyenkim.com/dong-ho-thong-minh-apple/"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(2))
                assert(splash:runjs('document.getElementsByClassName("nki-arow-rounded-next")[0].click();'))
                assert(splash:wait(5))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                headers=headers,
            )

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'}
        items = response.xpath('//*[@id="pagination_contents"]').css('div.item')
        for item in items:
            link = item.css('div.product-title a').attrib['href']
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            loai_man_hinh = ''
            chip = ''
            tinh_nang_khac = ''
            pin = ''
            bluetooth = ''
            ho_tro_sim = ''

            yield convert({
                'T??n s???n ph???m': item.css('div.product-title a::text').get(),
                "Gi?? s???n ph???m": str(item.css('p.final-price::text').get()).replace('??', ' VN??'),
                "Lo???i m??n h??nh": loai_man_hinh,
                "Chip": chip,
                "T??nh n??ng kh??c": tinh_nang_khac,
                "Pin": pin,
                "Bluetooth": bluetooth,
                "H??? tr??? sim": ho_tro_sim,
                "Link": link,
                'Th?? lo???i s???n ph???m': 'APPLE WATCH',
                'C???a h??ng': 'NGUYEN KIM',
            })

        yield SplashRequest(
            response.url,
            callback=self.parse,
            headers=headers,
            meta={
                "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
            },
        )


class nguyenkim_iphone(scrapy.Spider):
    name = 'nguyenkim_iphone'
    start_urls = ["https://www.nguyenkim.com/dien-thoai-di-dong-apple-iphone/"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(2))
                assert(splash:runjs('document.getElementsByClassName("nki-arow-rounded-next")[0].click();'))
                assert(splash:wait(5))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                headers=headers,
            )

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'}
        items = response.xpath('//*[@id="pagination_contents"]').css('div.item')
        for item in items:
            Ram = ''
            CPU = ''
            kich_thuoc_man_hinh = ''
            ROM = ''
            do_phan_giai_man_hinh = ''
            Pin = ''
            Camera_sau = ''
            Camera_truoc = ''
            bluetooth = ''
            link = item.css('div.product-title')[0].css('a').attrib['href']
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            try:
                informations = soup.find_all('table', class_='productSpecification_table')[1].find_all('tr')
                for information in informations:
                    if information.find('td', class_='title').text == 'Chipset:':
                        CPU = information.find('td', class_='value').text
                    elif information.find('td', class_='title').text == 'RAM:':
                        Ram = information.find('td', class_='value').text
                    elif information.find('td', class_='title').text == 'B??? nh??? trong:':
                        ROM = information.find('td', class_='value').text
                    elif information.find('td', class_='title').text == 'K??ch th?????c m??n h??nh:':
                        kich_thuoc_man_hinh = information.find('td', class_='value').text
                    elif information.find('td', class_='title').text == '????? ph??n gi???i m??n h??nh:':
                        do_phan_giai_man_hinh = information.find('td', class_='value').text
                    elif information.find('td', class_='title').text == 'Camera sau:':
                        Camera_sau = information.find('td', class_='value').text
                    elif information.find('td', class_='title').text == 'Camera tr?????c:':
                        Camera_truoc = information.find('td', class_='value').text
                    elif information.find('td', class_='title').text == 'Bluetooth:':
                        bluetooth = information.find('td', class_='value').text
            except:
                print("error " + str(link))
            yield convert({
                "T??n s???n ph???m": item.css('div.product-title a::text').get(),
                "Gi?? s???n ph???m": str(item.css('p.final-price::text').get()).replace('??', ' VN??'),
                "CPU": CPU,
                "Ram": Ram,
                "B??? nh??? trong": ROM,
                "K??ch th?????c m??n h??nh": kich_thuoc_man_hinh,
                "????? ph??n gi???i m??n h??nh": do_phan_giai_man_hinh,
                "Camera sau": Camera_sau,
                "Camera tr?????c": Camera_truoc,
                "Pin": Pin,
                "Bluetooth": bluetooth,
                "Link": link,
                'Th??? lo???i s???n ph???m': 'IPHONE',
                'C???a h??ng': 'NGUYEN KIM'
            })

        yield SplashRequest(
            response.url,
            callback=self.parse,
            headers=headers,
            meta={
                "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
            },
        )


class truesmart_iphone(scrapy.Spider):
    name = 'truesmart_iphone'
    start_urls = [
        "https://www.truesmart.com.vn/dien-thoai/iphone/",
        "https://www.truesmart.com.vn/iphone/page-2.html",
        "https://www.truesmart.com.vn/iphone/page-3.html",
        "https://www.truesmart.com.vn/iphone/page-4.html",
        "https://www.truesmart.com.vn/iphone/page-5.html"
    ]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(2))
                assert(splash:runjs('document.getElementsByClassName("nki-arow-rounded-next")[0].click();'))
                assert(splash:wait(5))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                headers=headers,
            )

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'}
        items = response.css('ul.pul')[0].css('li.c')
        for item in items:
            Ram = ''
            CPU = ''
            kich_thuoc_man_hinh = ''
            ROM = ''
            do_phan_giai_man_hinh = ''
            Pin = ''
            Camera_sau = ''
            Camera_truoc = ''
            bluetooth = ''
            link = 'https://www.truesmart.com.vn' + str(item.css('strong.t')[0].css('a').attrib['href'])
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            informations = soup.find('div', class_='cp1').find_all('tr')
            for information in informations:
                if str(information.find_all('td')[0].text).replace('\n', '').replace('\t', '') == 'B??? nh??? trong' or str(
                        information.find_all('td')[0].text).replace('\n', '').replace('\t', '') == 'B??? nh??? trong:':
                    ROM = information.find_all('td')[1].text
                elif str(information.find_all('td')[0].text).replace('\t', '').replace('\n',
                                                                                       '') == 'K??ch th?????c m??n h??nh' or \
                        str(information.find_all('td')[0].text).replace('\t', '').replace('\n',
                                                                                          '') == 'K??ch th?????c m??n h??nh:':
                    kich_thuoc_man_hinh = information.find_all('td')[1].text
                elif str(information.find_all('td')[0].text).replace('\t', '').replace('\n',
                                                                                       '') == '????? ph??n gi???i m??n h??nh' or \
                        str(information.find_all('td')[0].text).replace('\t', '').replace(
                            '\n', '') == '????? ph??n gi???i m??n h??nh:':
                    do_phan_giai_man_hinh = information.find_all('td')[1].text
                elif str(information.find_all('td')[0].text).replace('\t', '').replace('\n', '') == 'Dung l?????ng pin' or \
                        str(information.find_all('td')[0].text).replace('\t', '').replace('\n',
                                                                                          '') == 'Dung l????ng pin:' or \
                        str(information.find_all('td')[0].text).replace('\t', '').replace('\n', '') == 'Pin:' or \
                        str(information.find_all('td')[0].text).replace('\t', '').replace('\n', '') == 'Pin':
                    Pin = information.find_all('td')[1].text
                elif str(information.find_all('td')[0].text).replace('\t', '').replace('\n', '') == 'Camera sau:' or \
                        str(information.find_all('td')[0].text).replace('\t', '').replace('\n', '') == 'Camera sau':
                    Camera_sau = information.find_all('td')[1].text
                elif str(information.find_all('td')[0].text).replace('\t', '').replace('\n', '') == 'Camera tr?????c:' or \
                        str(information.find_all('td')[0].text).replace('\t', '').replace('\n', '') == 'Camera tr?????c':
                    Camera_truoc = information.find_all('td')[1].text
                elif str(information.find_all('td')[0].text).replace('\t', '').replace('\n', '') == 'CPU:' or \
                        str(information.find_all('td')[0].text).replace('\t', '').replace('\n', '') == 'CPU':
                    CPU = information.find_all('td')[1].text
                elif str(information.find_all('td')[0].text).replace('\t', '').replace('\n', '') == 'RAM:' or \
                        str(information.find_all('td')[0].text).replace('\t', '').replace('\n', '') == 'RAM':
                    Ram = information.find_all('td')[1].text

            yield convert({
                'T??n s???n ph???m': item.css('strong.t')[0].css('a::text').get(),
                'Gi?? s???n ph???m': str(item.css('b.b::text').get()).replace('???', 'VN??'),
                'B??? nh??? trong': ROM,
                '????? ph??n gi???i m??m h??nh': do_phan_giai_man_hinh,
                'K??ch th?????c mnaf h??nh': kich_thuoc_man_hinh,
                'Camera sau': Camera_sau,
                'Camera tr?????c': Camera_truoc,
                "CPU": CPU,
                "RAM": Ram,
                "Pin": Pin,
                'Link': link,
                'Th??? lo???i s???n ph???m':'IPHONE',
                'C???a h??ng': 'TRUE SMART'
            })


class iphone_24hstore(scrapy.Spider):
    name = 'iphone_24hstore'
    start_urls = ["https://24hstore.vn/dien-thoai-iphone-apple"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(1))
                assert(splash:runjs('for(var i = 0 ; i < 10 ; i ++){document.getElementById("load_more_button").click();}'))
                assert(splash:wait(5))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                headers=headers,
                meta={
                    "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
                },
            )

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

        items = response.xpath('//*[@id="box_product"]').css('div.product')
        for item in items:
            Ram = ''
            CPU = ''
            kich_thuoc_man_hinh = ''
            ROM = ''
            do_phan_giai_man_hinh = ''
            Pin = ''
            Camera_sau = ''
            Camera_truoc = ''
            bluetooth = ''
            link = item.css('div.frame_inner')[0].css('a').attrib['href']
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            try:
                # print(link)
                # print(len(soup.find_all('table', class_='charactestic_table_detail')))
                informations = soup.find_all('table', class_='charactestic_table_detail')[0].find_all('tr')
                for information in informations:
                    if information.find_all('td')[0].text.replace(' ', '').replace('\r', '').replace('\n',
                                                                                                     '') == 'M??nh??nhr???ng:':
                        kich_thuoc_man_hinh = information.find_all('td')[1].text.replace(' ', '').replace('\r',
                                                                                                          '').replace(
                            '\n', '')
                    elif information.find_all('td')[0].text.replace(' ', '').replace('\r', '').replace('\n',
                                                                                                       '') == '?????ph??ngi???i:':
                        do_phan_giai_man_hinh = information.find_all('td')[1].text.replace(' ', '').replace('\r',
                                                                                                            '').replace(
                            '\n', '')
                    elif information.find_all('td')[0].text.replace(' ', '').replace('\r', '').replace('\n',
                                                                                                       '') == 'Ram:':
                        Ram = information.find_all('td')[1].text.replace(' ', '').replace('\r',
                                                                                          '').replace(
                            '\n', '')
                    elif information.find_all('td')[0].text.replace(' ', '').replace('\r', '').replace('\n',
                                                                                                       '') == 'B???nh???trong:':
                        ROM = information.find_all('td')[1].text.replace(' ', '').replace('\r',
                                                                                          '').replace(
                            '\n', '')
                    elif information.find_all('td')[0].text.replace(' ', '').replace('\r', '').replace('\n',
                                                                                                       '') == 'CPU:':
                        CPU = information.find_all('td')[1].text.replace(' ', '').replace('\r',
                                                                                          '').replace(
                            '\n', '')
                    elif information.find_all('td')[0].text.replace(' ', '').replace('\r', '').replace('\n',
                                                                                                       '') == 'CameraSau:':
                        Camera_sau = information.find_all('td')[1].text.replace(' ', '').replace('\r',
                                                                                                 '').replace(
                            '\n', '')
                    elif information.find_all('td')[0].text.replace(' ', '').replace('\r', '').replace('\n',
                                                                                                       '') == 'Cameratr?????c:':
                        Camera_truoc = information.find_all('td')[1].text.replace(' ', '').replace('\r',
                                                                                                   '').replace(
                            '\n', '')
                    elif information.find_all('td')[0].text.replace(' ', '').replace('\r', '').replace('\n',
                                                                                                       '') == 'Dungl?????ngpin:':
                        Pin = information.find_all('td')[1].text.replace(' ', '').replace('\r',
                                                                                          '').replace(
                            '\n', '')
                    elif information.find_all('td')[0].text.replace(' ', '').replace('\r', '').replace('\n',
                                                                                                       '') == 'Bluetooth:':
                        bluetooth = information.find_all('td')[1].text.replace(' ', '').replace('\r',
                                                                                                '').replace(
                            '\n', '')

                yield convert({
                    'T??n s???n ph???m': item.css('div.name h3::text').get(),
                    'Gi?? s???n ph???m': str(item.css('span.price::text').get()).replace('??', ' VN??'),
                    'K??ch th?????c m??n h??nh': kich_thuoc_man_hinh,
                    '????? ph??n gi???i m??n h??nh': do_phan_giai_man_hinh,
                    'Ram': Ram,
                    'B??? nh??? trong': ROM,
                    'CPU': CPU,
                    'Camera sau': Camera_sau,
                    'Camera tr?????c': Camera_truoc,
                    'Pin': Pin,
                    'Bluetooth': bluetooth,
                    'Link': link,
                    'Th??? lo???i s???n ph???m': 'IPHONE',
                    'C???a h??ng':'24h STORE'
                })
            except:
                continue


class watch_24hstore(scrapy.Spider):
    name = 'watch_24hstore'
    start_urls = ["https://24hstore.vn/apple-watch-chinh-hang"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(1))
                assert(splash:runjs('for(var i = 0 ; i < 10 ; i ++){document.getElementById("load_more_button").click();}'))
                assert(splash:wait(5))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                headers=headers,
                meta={
                    "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
                },
            )

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

        items = response.xpath('//*[@id="box_product"]').css('div.product')
        for item in items:
            loai_man_hinh = ''
            chip = ''
            tinh_nang_khac = ''
            pin = ''
            bluetooth = ''
            ho_tro_sim = ''
            link = item.css('div.frame_inner')[0].css('a').attrib['href']
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            try:
                informations = soup.find_all('table', class_='charactestic_table_detail')[0].find_all('tr')
                for information in informations:
                    if information.find_all('td')[0].text.replace(' ', '').replace('\r', '').replace('\n',
                                                                                                     '') == 'M??nh??nh:':
                        loai_man_hinh = information.find_all('td')[1].text.replace(' ', '').replace('\r',
                                                                                                    '').replace(
                            '\n', '')
                    elif information.find_all('td')[0].text.replace(' ', '').replace('\r', '').replace('\n',
                                                                                                       '') == 'CPU:':
                        chip = information.find_all('td')[1].text.replace(' ', '').replace('\r',
                                                                                           '').replace(
                            '\n', '')
                    elif information.find_all('td')[0].text.replace(' ', '').replace('\r', '').replace('\n',
                                                                                                       '') == 'Dungl?????ngPin:':
                        pin = information.find_all('td')[1].text.replace(' ', '').replace('\r',
                                                                                          '').replace(
                            '\n', '')
                    elif information.find_all('td')[0].text.replace(' ', '').replace('\r', '').replace('\n',
                                                                                                       '') == 'SIM:':
                        ho_tro_sim = information.find_all('td')[1].text.replace(' ', '').replace('\r',
                                                                                                 '').replace(
                            '\n', '')
                    elif information.find_all('td')[0].text.replace(' ', '').replace('\r', '').replace('\n',
                                                                                                       '') == 'K???tn???i:':
                        bluetooth = information.find_all('td')[1].text.replace(' ', '').replace('\r',
                                                                                                '').replace(
                            '\n', '')

                yield convert({
                    'T??n s???n ph???m': item.css('div.name h3::text').get(),
                    'Gi?? s???n ph???m': str(item.css('span.price::text').get()).replace('??', ' VN??'),
                    'lo???i m??n h??nh': loai_man_hinh,
                    'Chip': chip,
                    'Pin': pin,
                    'Sim': ho_tro_sim,
                    'Bluetooth': bluetooth,
                    'T??nh n??ng': tinh_nang_khac,
                    'Link': link,
                    'Th??? lo???i s???n ph???m':'APPLE WATCH',
                    'C???a h??ng':'24H STORE'
                })
            except:
                continue


class xtsmart_iphone(scrapy.Spider):
    name = 'xtsmart_iphone'
    start_urls = ["https://www.xtsmart.vn/apple"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(1))
                assert(splash:runjs('for(var i = 0 ; i < 10 ; i ++){document.getElementsByClassName("pagination-more")[0].getElementsByTagName("i")[0].click()}'))
                assert(splash:wait(5))
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                headers=headers,
                meta={
                    "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
                },
            )

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

        items = response.xpath('//*[@id="List_Product"]').css('div.product-base-grid')
        for item in items:
            Ram = ''
            CPU = ''
            kich_thuoc_man_hinh = ''
            ROM = ''
            do_phan_giai_man_hinh = ''
            Pin = ''
            Camera_sau = ''
            Camera_truoc = ''
            bluetooth = ''
            link = item.css('h3 a').attrib['href']
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            informations = soup.find('ul', class_='paraexpand').find_all('li')
            for information in informations:
                try:
                    if information.find('span').text == 'Chipset (h??ng SX CPU)':
                        CPU = information.find('strong').text
                    elif information.find('span').text == 'RAM':
                        Ram = information.find('strong').text
                    elif information.find('span').text == 'B??? nh??? trong':
                        ROM = information.find('strong').text
                    elif information.find('span').text == 'Bluetooth':
                        bluetooth = information.find('strong').text
                    elif information.find('span').text == 'M??n h??nh r???ng':
                        kich_thuoc_man_hinh = information.find('strong').text
                    elif information.find('span').text == '????? ph??n gi???i':
                        do_phan_giai_man_hinh = information.find('strong').text
                    elif information.find('span').text == 'Dung l?????ng pin':
                        Pin = information.find('strong').text

                except:
                    continue
            yield convert({
                "T??n s???n ph???m": item.css('h3 a::text').get(),
                "Gi?? s???n ph???m": item.css('div.price::text').get().replace('??', 'VN??'),
                'CPU': CPU,
                'RAM': Ram,
                "B??? nh??? trong": ROM,
                "K??ch th?????c m??n h??nh": kich_thuoc_man_hinh,
                "????? ph??n gi???i m??n h??nh": do_phan_giai_man_hinh,
                'Pin': Pin,
                "Bluetooth": bluetooth,
                "Camera sau": Camera_sau,
                'Camera tr?????c': Camera_truoc,
                "Link": link,
                'Th??? lo???i s???n ph???m':'IPHONE',
                'C???a h??ng': 'XTSMART'
            })


class didongthongminh_iphone(scrapy.Spider):
    name = 'didongthongminh_iphone'
    start_urls = ["https://didongthongminh.vn/iphone"]
    script = """
            function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                assert(splash:wait(1))
                assert(splash:runjs('document.getElementsByClassName("lmp_button")[0].click()'))
                assert(splash:wait(1))
                assert(splash:runjs('document.getElementsByClassName("lmp_button")[0].click()'))
                assert(splash:wait(1))
                assert(splash:runjs('document.getElementsByClassName("lmp_button")[0].click()'))
                assert(splash:wait(1))
                assert(splash:runjs('document.getElementsByClassName("lmp_button")[0].click()'))
                assert(splash:wait(1))
                assert(splash:runjs('document.getElementsByClassName("lmp_button")[0].click()'))
                assert(splash:wait(1))
                assert(splash:runjs('document.getElementsByClassName("lmp_button")[0].click()'))
                assert(splash:wait(1))
                assert(splash:runjs('document.getElementsByClassName("lmp_button")[0].click()'))
                assert(splash:wait(1))
                assert(splash:runjs('document.getElementsByClassName("lmp_button")[0].click()'))
                assert(splash:wait(1))
                assert(splash:runjs('document.getElementsByClassName("lmp_button")[0].click()'))
                assert(splash:wait(1))
                
                return {
                    html = splash:html(),
                    url = splash:url(),
                }
            end
            """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                headers=headers,
                meta={
                    "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
                },
            )

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

        items = response.xpath('//*[@id="main"]/ul').css('li.col-6')

        for item in items:
            Ram = ''
            CPU = ''
            kich_thuoc_man_hinh = ''
            ROM = ''
            do_phan_giai_man_hinh = ''
            Pin = ''
            Camera_sau = ''
            Camera_truoc = ''
            bluetooth = ''
            link = item.css('a.woocommerce-LoopProduct-link').attrib['href']
            req = requests.get(link, headers=headers)
            soup = BeautifulSoup(req.text, "lxml")
            informations = soup.find('table', class_='shop_attributes').find_all('tr')
            for information in informations:
                try:
                    if information.find('th').text == 'M??n h??nh':
                        kich_thuoc_man_hinh = information.find('a').text
                    elif information.find('th').text == 'CPU':
                        CPU = information.find('a').text
                    elif information.find('th').text == 'RAM':
                        Ram = information.find('a').text
                    elif information.find('th').text == 'B??? nh??? trong':
                        ROM = information.find('a').text
                    elif information.find('th').text == 'Camera sau':
                        Camera_sau = information.find('a').text
                    elif information.find('th').text == 'Camera tr?????c':
                        Camera_truoc = information.find('a').text
                    elif information.find('th').text == 'Pin':
                        Pin = information.find('a').text
                    elif information.find('th').text == 'Bluetooth':
                        bluetooth = information.find('a').text
                except:
                    continue
            yield convert({
                "T??n s???n ph???m": item.css('span.dst_primtitle::text').get(),
                "Gi?? s???n ph???m": item.css('span.woocommerce-Price-amount::text').get() + ' VN??',
                'CPU': CPU,
                'RAM': Ram,
                "B??? nh??? trong": ROM,
                "K??ch th?????c m??n h??nh": kich_thuoc_man_hinh,
                "????? ph??n gi???i m??n h??nh": do_phan_giai_man_hinh,
                'Pin': Pin,
                "Bluetooth": bluetooth,
                "Camera sau": Camera_sau,
                'Camera tr?????c': Camera_truoc,
                "Link": link,
                'Th??? lo???i s???n ph???m':'IPHONE',
                'C???a h??ng':'DI DONG THONG MINH',
            })
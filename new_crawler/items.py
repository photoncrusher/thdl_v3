import scrapy
from scrapy.item import Field

# productionItems: lược đồ khi mới crawl về
# schemaItems: lược đồ chuẩn

class productItems(scrapy.Item):
    pass

class schemaItems(scrapy.Item):
    name = Field()
    color = Field()
    status = Field()    # cũ, mới
    resolution = Field()
    screentech = Field()
    screensize = Field()
    rear_cam = Field()
    front_cam = Field()
    pin = Field()
    sim = Field()
    cpu = Field()
    ram = Field()
    rom = Field()
    os = Field()
    gpu = Field()
    size = Field()
    weigth = Field()
    tech = Field()
    wifi = Field()
    bluetooth = Field()
    port = Field()
    price = Field()
    link = Field()
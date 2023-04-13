# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertysalebdItem(scrapy.Item):
    title = scrapy.Field()
    property_name = scrapy.Field()
    property_type = scrapy.Field()
    property_for = scrapy.Field()
    location = scrapy.Field()
    address = scrapy.Field()
    construction_status = scrapy.Field()
    property_size = scrapy.Field()
    price_per_sqft_or_katha_or_dcml = scrapy.Field()
    monthly_rent = scrapy.Field()
    total_price = scrapy.Field()
    deposit = scrapy.Field()
    transaction_type = scrapy.Field()
    bedroom = scrapy.Field()
    balconies = scrapy.Field()
    bathroom = scrapy.Field()
    floor_number = scrapy.Field()
    garages = scrapy.Field()
    total_floor = scrapy.Field()
    furnishing = scrapy.Field()
    facing = scrapy.Field()
    land_area = scrapy.Field()
    handover_date = scrapy.Field()
    available_from = scrapy.Field()
    description = scrapy.Field()
    amenities = scrapy.Field()
    facilities_nearby = scrapy.Field()
    property_url = scrapy.Field()


# Scrapy settings for scrapy_superhero project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scrapy_superhero'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['scrapy_superhero.spiders']
NEWSPIDER_MODULE = 'scrapy_superhero.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
  'scrapymongodb.MongoDBPipeline',
]

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'test'
MONGODB_COLLECTION = 'superheroes'
#MONGODB_UNIQ_KEY = 'url'
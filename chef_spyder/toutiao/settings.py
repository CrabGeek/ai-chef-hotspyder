DOWNLOADER_MIDDLEWARES = {
    "middlewares.TouTiaoHotListPageDownloaderMiddleware": 100,
    "middlewares.TouTiaoArticleDownloaderMiddleware": 200,
}

ITEM_PIPELINES = {
    "pipelines.TouTiaoPipeline": 100,
}

LOG_LEVEL = "INFO"

ROBOTSTXT_OBEY = False

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
# FEED_EXPORT_ENCODING = "UTF-8"


SElENIUM_OPTIONS = ["--headless", "--log-level=3"]

SELENUM_REQUEST_TIMEOUT = 60
from datameta.core import celery, catalogs

from datameta.crawlers.ckan import CkanPackageCrawler, CkanIndexCrawler

CRAWLERS = (CkanPackageCrawler, CkanIndexCrawler)


def queue_all():
    for name, config in catalogs.items():
        crawler = config.get('crawler')
        config['name'] = name
        run_crawler.delay(crawler, config)


def crawlers():
    crawlers = {}
    for crawler in CRAWLERS:
        crawlers[crawler.get_name()] = crawler
    return crawlers


@celery.task()
def run_crawler(name, item):
    cls = crawlers().get(name)
    cls().process(item)

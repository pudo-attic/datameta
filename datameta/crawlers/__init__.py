from datameta.core import celery, catalogs

from datameta.crawlers.ckan import CkanPackageCrawler, CkanIndexCrawler
from datameta.crawlers.socrata import SocrataIndexCrawler
from datameta.crawlers.socrata import SocrataDatasetCrawler


CRAWLERS = (CkanPackageCrawler, CkanIndexCrawler,
            SocrataIndexCrawler, SocrataDatasetCrawler)


def queue_all(catalog=None):
    for name, config in catalogs.items():
        if catalog is not None and catalog != name:
            continue
        crawler = config.get('crawler')
        config['name'] = name
        run_crawler.delay(crawler, config.copy())


def crawlers():
    crawlers = {}
    for crawler in CRAWLERS:
        crawlers[crawler.get_name()] = crawler
    return crawlers


@celery.task()
def run_crawler(name, item):
    cls = crawlers().get(name)
    cls().process(item)

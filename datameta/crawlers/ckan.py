
import requests

from datameta.crawlers.base import Crawler


class CkanPackageCrawler(Crawler):

    def process(self, item):
        res = requests.get(item.get('url'))
        print res.json()


class CkanIndexCrawler(Crawler):
    name = 'ckan'

    def process(self, item):
        api_base = item.get('api')
        pkg_list = '%s/2/rest/dataset' % api_base
        res = requests.get(pkg_list)
        for pkg_id in res.json():
            url = '%s/%s' % (pkg_list, pkg_id)
            item = {'catalog': item, 'url': url}
            CkanPackageCrawler.schedule(item)

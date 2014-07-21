
import requests

from datameta.crawlers.base import Crawler


class CkanPackageCrawler(Crawler):

    def process(self, item):
        res = requests.get(item.get('url'))
        data = res.json()
        dataset = {
            'id': data.get('id'),
            'slug': data.get('name'),
            'title': data.get('title'),
            'tags': data.get('tags'),
            'status': data.get('state'),
            'catalog': item.get('catalog'),
            'created_at': data.get('metadata_created'),
            'modified_at': data.get('metadata_modified'),
            'metadata_url': data.get('ckan_url'),
            'api_url': item.get('url'),
            'description': data.get('notes_rendered'),
            'creator': None,
            'publisher': None,
            'raw': data,
            'distributions': []
        }
        for res in data.get('resources'):
            dataset['distributions'].append({
                'url': res.get('url'),
                'mimetype': res.get('mimetype')
            })


class CkanIndexCrawler(Crawler):
    name = 'ckan'

    def process(self, item):
        api_base = item.get('api')
        pkg_list = '%s/api/2/rest/dataset' % api_base
        res = requests.get(pkg_list)
        for pkg_id in res.json():
            url = '%s/%s' % (pkg_list, pkg_id)
            i = {'catalog': item, 'url': url}
            CkanPackageCrawler.schedule(i)

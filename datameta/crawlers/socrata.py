from datetime import datetime
import pytz
from itertools import count
import requests

from datameta.crawlers.base import Crawler


def convert_time(ts):
    dt = datetime.fromtimestamp(ts, tz=pytz.utc)
    return dt.isoformat()


class SocrataDatasetCrawler(Crawler):

    def process(self, item):
        api_base = item.get('catalog').get('api')
        data = item.get('dataset')
        dataset = {
            'id': data.get('oid'),
            'slug': data.get('id'),
            'title': data.get('name'),
            'tags': data.get('tags'),
            'status': data.get('publicationStage'),
            'catalog': item.get('catalog'),
            'created_at': convert_time(data.get('createdAt')),
            'modified_at': convert_time(data.get('viewLastModified')),
            'metadata_url': '%s/d/%s' % (api_base, data.get('id')),
            'creator': data.get('tableAuthor', {}).get('displayName'),
            'publisher': data.get('owner', {}).get('displayName'),
            'raw': data,
            'distributions': []
        }
        if data.get('displayType') == 'table' or \
                data.get('viewType') == 'tabular':
            dataset['distributions'].append({
                'url': '%s/resource/%s.csv' % (api_base, data.get('id')),
                'mimetype': 'text/csv'
            })
        print dataset


class SocrataIndexCrawler(Crawler):
    name = 'socrata'

    def process(self, item):
        api_base = item.get('api')
        for i in count(1):
            ds_list = '%s/api/views?page=%s' % (api_base, i)
            res = requests.get(ds_list)
            data = res.json()
            if not len(data):
                return
            for ds in data:
                i = {'catalog': item, 'dataset': ds}
                SocrataDatasetCrawler.schedule(i)

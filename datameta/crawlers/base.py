

class Crawler(object):

    def process(self, item):
        pass

    @classmethod
    def get_name(cls):
        if hasattr(cls, 'name'):
            return cls.name
        return cls.__name__

    @classmethod
    def schedule(cls, item):
        from datameta.crawlers import run_crawler
        run_crawler.delay(cls.get_name(), item)

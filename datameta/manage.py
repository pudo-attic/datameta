from flask.ext.script import Manager

from datameta.core import app, celery
from datameta.crawlers import queue_all

manager = Manager(app)


@manager.command
def fetch():
    """ Fetch data from all catalogs """
    queue_all()

if __name__ == '__main__':
    manager.run()

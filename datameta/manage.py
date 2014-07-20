from flask.ext.script import Manager

from datameta.core import app

manager = Manager(app)


@manager.command
def fetch():
    """ Fetch data from all catalogs """
    pass

if __name__ == '__main__':
    manager.run()

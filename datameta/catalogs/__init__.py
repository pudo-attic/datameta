import yaml


def load_catalogs(app):
    with app.open_resource('catalogs.yaml', 'r') as fh:
        return yaml.load(fh)

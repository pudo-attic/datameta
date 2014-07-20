from kombu import Exchange, Queue

DEBUG = True

CELERY_ACCEPT_CONTENT = ['json']
CELERY_IGNORE_RESULT = True

CELERY_BROKER_URL = 'sqla+postgresql://localhost/celery'

CELERY_DEFAULT_QUEUE = 'datameta'
CELERY_QUEUES = (
    Queue('datameta', Exchange('datameta'), routing_key='datameta'),
)
CELERY_TASK_SERIALIZER = 'json'

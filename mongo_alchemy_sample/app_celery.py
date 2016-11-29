from celery import Celery

from mongo_alchemy_sample.app import create_app
from mongo_alchemy_sample.settings import PROJECT_APPS

flask_app = create_app('Development')
celery_app = Celery(flask_app.import_name, broker=flask_app.config['CELERY_BROKER_URL'])
celery_app.conf.update(flask_app.config)
TaskBase = celery_app.Task


class ContextTask(TaskBase):
    abstract = True

    def __call__(self, *args, **kwargs):
        with flask_app.app_context():
            return TaskBase.__call__(self, *args, **kwargs)


celery_app.Task = ContextTask
celery_app.autodiscover_tasks(lambda: PROJECT_APPS)

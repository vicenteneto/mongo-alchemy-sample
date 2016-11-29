from mongo_alchemy_sample import celery_app


@celery_app.task()
def add_(a, b):
    print a + b

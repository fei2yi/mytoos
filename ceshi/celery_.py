import time

from celery import Celery

celery = Celery('celery_', broker='redis://47.95.249.180:6379/3')

@celery.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')




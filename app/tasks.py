from __future__ import absolute_import
from celery import task
from celery import shared_task
from app import models
import datetime

@task
def test_celery(x, y):
    models.CeleryModels.objects.create(time=datetime.datetime.now())
    print("参数相加结果:",x+y)
    return "我是测试函数"

@shared_task()
def sub():
    models.CeleryModels.objects.create(time=datetime.datetime.now(),name="cox")
    return "我是测试函数22222"



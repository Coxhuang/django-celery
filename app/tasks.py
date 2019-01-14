from __future__ import absolute_import
from celery import task
from app import models
import datetime

@task
def test_celery(x, y):
    models.CeleryModels.objects.create(time=datetime.datetime.now())
    print("参数相加结果:",x+y)
    return "我是测试函数"



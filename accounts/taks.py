from __future__ import absolute_import, unicode_literals
from .celery import app
from .models import User


# @app.task
# def add(x, y):
#     return x + y


# @app.task
# def mul(x, y):
#     return x * y


# @app.task
# def xsum(numbers):
#     return sum(numbers)
@app.task(serializer='json')
def create_user(username, password):
    User.objects.create(username=username, password=password)    
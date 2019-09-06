# <<<<<<< HEAD
# import logging
 
# from django.urls import reverse
# from django.core.mail import send_mail
# from django.contrib.auth import get_user_model
# from quick_publisher.celery import app
 
 
# @app.task
# def send_verification_email(user_id):
#     UserModel = get_user_model()
#     try:
#         user = UserModel.objects.get(pk=user_id)
#         send_mail(
#             'Verify your QuickPublisher account',
#             'Follow this link to verify your account: '
#                 'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
#             'from@quickpublisher.dev',
#             [user.email],
#             fail_silently=False,
#         )
#     except UserModel.DoesNotExist:
#         logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)
# =======
# from __future__ import absolute_import, unicode_literals
# from .celery import app
# from celery import Celery
# # from .models import User

# # @app.task
# # def create_user(username, password):
# #     User.objects.create(username=username, password=password)

# app = Celery('accounts',broker='amqp://localhost//',)

# @app.task
# def add(x, y):
#     return x + y


# @app.task
# def mul(x, y):
#     return x * y


# @app.task
# def xsum(numbers):
#     return sum(numbers)
    
# >>>>>>> c23780c21d620240d733d35107e75dc0d79d052b

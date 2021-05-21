from django.contrib import admin
from .models import Article
import firebase_admin
from firebase_admin import credentials 
from firebase_admin import db
from firebase_admin import messaging
import datetime


# cred = credentials.Certificate('C:/Users/Khsbyr/Desktop/eass/firebase-sdk.json')

# firebase_admin.initialize_app(cred, {
#     'databaseURL' : 'https://easbackend-default-rtdb.firebaseio.com/'
# })

admin.site.register(Article)
# registration_token = 'fLw6KfRMiT5K7yFLNZ-_G9:APA91bHrfLs-6YxjJewNKmFi2ynEGR1eJm2YP7fMh4nSmXiTg8dYeMK2bJ-bwwfjfzOvLV1pJcsDoViY--O0ipdIyjaQdEOJWWigz8uRMelYZ1F4iqRO2Tw2Ux4TP3sCJdS0xBqQJUT_'
# message = messaging.Message(
#     notification=messaging.Notification(
#         title='hi',
#         body='hii',
#     ),
#     token=registration_token,
#     )
# response = messaging.send(message)
# print('Successfully sent message:', response)

# class MyAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, changed):
#         if '_continue' in request.POST:
#             registration_token = 'fLw6KfRMiT5K7yFLNZ-_G9:APA91bHrfLs-6YxjJewNKmFi2ynEGR1eJm2YP7fMh4nSmXiTg8dYeMK2bJ-bwwfjfzOvLV1pJcsDoViY--O0ipdIyjaQdEOJWWigz8uRMelYZ1F4iqRO2Tw2Ux4TP3sCJdS0xBqQJUT_'
#             message = messaging.Message(
#                 notification=messaging.Notification(
#                     title='hi',
#                     body='hii',
#                 ),
#                 token=registration_token,
#                 )
#             response = messaging.send(message)
#             print('Successfully sent message:', response)
#         return super(ServerAdmin, self).change_view(request, obj, form, changed)
# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ("title", "date")
#     actions = ['send_notif']

    
#     def send_notif(self, request, queryset):  
#         registration_token = 'fLw6KfRMiT5K7yFLNZ-_G9:APA91bHrfLs-6YxjJewNKmFi2ynEGR1eJm2YP7fMh4nSmXiTg8dYeMK2bJ-bwwfjfzOvLV1pJcsDoViY--O0ipdIyjaQdEOJWWigz8uRMelYZ1F4iqRO2Tw2Ux4TP3sCJdS0xBqQJUT_'
#         message = messaging.Message(
#             notification=messaging.Notification(
#                 title=Article['title'],
#                 body='hii',
#             ),
#             token=registration_token,
#             )
#         response = messaging.send(message)
#         print('Successfully sent message:', response)
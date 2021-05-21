import firebase_admin
from firebase_admin import credentials 
from firebase_admin import db
from firebase_admin import messaging
import datetime


cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://easbackend-default-rtdb.firebaseio.com/'
})

# ref = db.reference('/')
# ref.set({
#     'Article':
#         {
#             'title': 'asdasd',
#             'date': '2021-04-20',
#         }

# })

registration_token = 'fLw6KfRMiT5K7yFLNZ-_G9:APA91bHrfLs-6YxjJewNKmFi2ynEGR1eJm2YP7fMh4nSmXiTg8dYeMK2bJ-bwwfjfzOvLV1pJcsDoViY--O0ipdIyjaQdEOJWWigz8uRMelYZ1F4iqRO2Tw2Ux4TP3sCJdS0xBqQJUT_'

# See documentation on defining a message payload.
message = messaging.Message(
    notification=messaging.Notification(
        title='NOTIF',
        body='HII',
    ),
    token=registration_token,
)

response = messaging.send(message)
print('Successfully sent message:', response)
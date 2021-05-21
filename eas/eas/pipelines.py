import mysql.connector
import firebase_admin
from firebase_admin import credentials 
from firebase_admin import db
from firebase_admin import messaging
import datetime


cred = credentials.Certificate('C:/Users/Khsbyr/Desktop/eass/firebase-sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://easbackend-default-rtdb.firebaseio.com/'
})


class EasPipeline(object):

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = '0808',
            database = 'eas_db'
        )
        self.curr = self.conn.cursor()


    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        self.curr.execute("""insert into articles_article (title, date, description) values (%s, %s, %s)""", (
            item['title'],
            item['date'],
            item['description']
        ))
        self.conn.commit()

        
        registration_token = 'fLw6KfRMiT5K7yFLNZ-_G9:APA91bHrfLs-6YxjJewNKmFi2ynEGR1eJm2YP7fMh4nSmXiTg8dYeMK2bJ-bwwfjfzOvLV1pJcsDoViY--O0ipdIyjaQdEOJWWigz8uRMelYZ1F4iqRO2Tw2Ux4TP3sCJdS0xBqQJUT_'
        message = messaging.Message(
            notification=messaging.Notification(
                title=item['title'],
                body=item['date'],
            ),
            token=registration_token,
            )
        response = messaging.send(message)
        print('Successfully sent message:', response)

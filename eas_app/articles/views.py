from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article
import firebase_admin
from firebase_admin import credentials 
from firebase_admin import db
from firebase_admin import messaging
import datetime

cred = credentials.Certificate('C:/Users/Khsbyr/Desktop/eass/firebase-sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://easbackend-default-rtdb.firebaseio.com/'
})



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/article-list/',
        'Detail View':'/article-detail/<str:pk>/',
        'Create':'/article-create/',
        'Update':'/article-update/<str:pk>/',
        'Delete':'/article-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def ViewArticle(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(article, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateArticle(request):
    serializer = ArticleSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    registration_token = 'fLw6KfRMiT5K7yFLNZ-_G9:APA91bHrfLs-6YxjJewNKmFi2ynEGR1eJm2YP7fMh4nSmXiTg8dYeMK2bJ-bwwfjfzOvLV1pJcsDoViY--O0ipdIyjaQdEOJWWigz8uRMelYZ1F4iqRO2Tw2Ux4TP3sCJdS0xBqQJUT_'
    message = messaging.Message(
        notification=messaging.Notification(
            title=request.data['title'],
            body=request.data['date'],
        ),
        token=registration_token,
        )
    response = messaging.send(message)
    print('Successfully sent message:', response)


    return Response(serializer.data)


@api_view(['POST'])
def updateArticle(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(instance=article, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteArticle(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return Response('Amjilttai ustgagdlaa!')
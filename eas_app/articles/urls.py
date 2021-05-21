from django.urls import path
from . import views
urlpatterns = [
    path('', views.apiOverview, name="apiOverview"),
    path('article-list/', views.ShowAll, name="article-list"),
    path('article-detail/<int:pk>', views.ViewArticle, name="article-detail"),
    path('article-create/', views.CreateArticle, name="article-create"),
    path('article-update/<int:pk>', views.updateArticle, name="article-update"),
    path('article-delete/<int:pk>', views.deleteArticle, name="article-delete"),
]
from django.urls import path
from . import views

app_name = 'blog'
# 第一个参数用了正则表达式，第二个参数是视图函数，第三个参数是视图参数的别名
urlpatterns = [
    path('', views.ocr, name = 'ocr'),
    path(r'^post/(?p<pk>[0-9]+)/$', views.detail, name = 'detail'),
]
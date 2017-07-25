from django.conf.urls import url,include
from . import views

urlpatterns = [
    url('^$',views.index,name='index'),
    url('^csvreader_post', views.csv_post, name='csv_post')

]
from django.conf.urls import urls
from album import views

urlpatterns =[

	url(r'^$',views.index,name='index'),
]
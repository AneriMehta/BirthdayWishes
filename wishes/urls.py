from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.welcome, name = 'welcome'),
    url(r'^cards/$', views.cards, name='cards'),
    url(r'^cards/(?P<pk>\d+)/$', views.card, name='card'),
]

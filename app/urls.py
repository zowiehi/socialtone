from django.conf.urls import url

from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.MainPage.as_view(), name='index'),
    url(r'^search$', views.ResultsPage.as_view(), name='search'),
    url(r'^api$', views.scrape_all, name='api')
]

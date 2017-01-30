from django.conf.urls import url

from . import views
from . import admin_views


app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^admin/polls/results$', admin_views.results, name='results'),
]

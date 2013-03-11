from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'demosite.views.index'),
    url(r'^500$', 'demosite.views.gimme500'),
)

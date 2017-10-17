from django.conf.urls import url

from newmahendrasheraone import views

urlpatterns = [
url(r'^$',views.home, name='home'),
url(r'^test/$',views.testSimple, name='test'),
url(r'^test/(?P<testno>[0-9]+)/$',views.testSimpleUrlpath, name='urlpathtest'),

]

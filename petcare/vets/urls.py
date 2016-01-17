from django.conf.urls import url


from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^find/',views.search_by_place,name='search'),
    url(r'^(?P<lat>\d*[.]?\d+)/(?P<lon>\d*[.]?\d+)',views.locate_around_me,name='locate'),  

]
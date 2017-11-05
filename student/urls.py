from django.conf.urls import include, url

from student import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^forum/', include('qaforum.urls')),
    url(r'^classmates/$', views.classmates, name = 'view_classmates'),
    url(r'^profile/$', views.view_profile, name = 'view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name = 'view_profile_with_pk'),
    url(r'^profile/edit/$', views.edit_profile, name = 'edit_profile'),
    url(r'^(?P<course_No>.+)/forum/', include('qa.urls')),
    url(r'^(?P<course_No>.+)/$', views.sem_course, name = 'sem_course'),


]

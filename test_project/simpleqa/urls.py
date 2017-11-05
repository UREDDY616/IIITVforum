from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from core.views import register, user_login, user_logout


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^student/', include('student.urls')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

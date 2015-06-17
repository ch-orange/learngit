#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf  import settings 
from app01.upload  import   upload_image
#from app01  import views
import app01.urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'',include(app01.urls)),
    url(r"^uploads/(?P<path>.*)$", \
                "django.views.static.serve", \
                {"document_root": settings.MEDIA_ROOT,}),
     url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
)

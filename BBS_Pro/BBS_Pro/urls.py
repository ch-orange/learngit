from django.conf.urls import patterns, include, url
from django.contrib import admin
#from app01  import views
import app01.urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   url(r'',include(app01.urls)),
)

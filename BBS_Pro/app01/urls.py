from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^accoutslogin/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    (r'^login/$',views.login),
    #url(r'^$',views.register,name='register'),
    url(r'^acc_login/$',views.acc_login),
    (r'^logout/$',views.logout_view),
    (r'^$', views.index),
    (r'^detail/(\d+)/$', views.bbs_detail),
     (r'^sub_comment/$', views.sub_comment),
     (r'^bbs_pub/$', views.bbs_pub),
    (r'^bbs_sub/$', views.bbs_sub),
    (r'^category/(\d+)/$', views.category),
                       
    
)

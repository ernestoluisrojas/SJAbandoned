from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blight_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mvp_app.views.home', name='home'),
    url(r'^test/$', 'mvp_app.views.test', name='test'),
    url(r'^index/$', 'mvp_app.views.index', name='index'),
    url(r'^properties/', include('blight_app.urls')),
)

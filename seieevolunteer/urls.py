from django.conf.urls import patterns, include, url
from seieevolunteer import views
from django.contrib import admin
from django.contrib.auth.views import login,logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'seieevolunteer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/',include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^signup/$',views.signup),
    url(r'^login/$', login),
    url(r'^logout/$',logout),
    url(r'^sign_info/',views.sign_info),
    url(r'^signup_info_back/',views.signup_info_back),
    url(r'^signup/thanks/$',views.thanks),
    url(r'^lookup/$',views.lookup),
    url(r'^lookup_result/$',views.lookup_result),
    url(r'^contact/$',views.contact),
    url(r'^contact/reply/$',views.contact_reply),
    url(r'^contact/thanks/$',views.thanks),
)

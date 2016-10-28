from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import slack.oauth

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth', slack.oauth.oauth),
    url(r'^newdb', slack.oauth.newdb),
    url(r'^poll/(?P<pollName>\w+)/', slack.oauth.poll)
]

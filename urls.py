from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.homepage'),                   
    url(r'^wiki/$', 'views.wiki'),
    url(r'^contact/$', 'views.contact'),
    url(r'^ident/(?P<club_id>\d+)/$', 'ident.views.ident'),
    url(r'^board/(?P<club_id>\d+)/$', 'ident.views.board'),
    url(r'^budget/(?P<club_id>\d+)/$', 'budget.views.budget'),
    url(r'^teams/$', 'team.views.teams'),
    url(r'^team/(?P<team_id>\d+)/$', 'team.views.team'),
    url(r'^team_new/$', 'team.views.team_new'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),
    
)
urlpatterns += patterns('',
    url(r'^media/(.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)

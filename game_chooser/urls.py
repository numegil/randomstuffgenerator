from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'game_chooser.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'chooser.views.get_random_game', name='get_random_game'),
    url(r'^page$', 'chooser.views.get_random_page', name='get_random_page'),
    url(r'^escape$', 'chooser.views.escape', name='escape'),
]

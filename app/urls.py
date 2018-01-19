from django.conf.urls import url
from .api import snippets
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets$', snippets.snippet_list),
    url(r'^snippets/snippet_list$', snippets.Snippets.getsa),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', snippets.snippet_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
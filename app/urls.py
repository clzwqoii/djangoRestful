from django.conf.urls import url
from .api import message
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^message', message.message_list),
    url(r'^message/message_list$', message.Messages.getsa),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', snippets.snippet_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
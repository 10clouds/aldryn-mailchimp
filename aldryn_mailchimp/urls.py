# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import campaign_detail


urlpatterns = [
    url(
        r'^(?P<pk>[0-9]+)/(?P<slug>[\w.@+-]+)/$',
        campaign_detail,
        name='mailchimp_campaign_detail'
    ),
]

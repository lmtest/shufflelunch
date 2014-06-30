# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'web.views',

    url(r'^$', 'top'),
)

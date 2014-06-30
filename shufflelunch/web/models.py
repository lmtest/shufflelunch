# -*- coding: utf-8 -*-

from django.db import models


class EnabledManager(models.Manager):
    def get_query_set(self):
        q = super(EnabledManager, self).get_query_set()
        return q.filter(enabled=True)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = models.Manager()
    enableds = EnabledManager()

    enabled = models.BooleanField(u'有効', default=True)
    created = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated = models.DateTimeField(u'更新日時', auto_now=True)

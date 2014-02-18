# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


class Template(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(_("Template File Name"), max_length=250)


class BaseFormPlugin(CMSPlugin):
    def __str__(self):
        return self.template.name

    template = models.ForeignKey(Template, verbose_name=_("Template"))

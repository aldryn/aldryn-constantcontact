# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.conf.urls import patterns, url

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import BaseFormPlugin
from .forms import BaseFormPluginForm
from .views import submit_form


class ConstantContactBase(CMSPluginBase):
    module = 'Constant Contact'


class EmailFormCMSPlugin(ConstantContactBase):
    render_template = 'aldryn_constantcontact/plugins/base.html'
    name = _('Constant Contact Form')
    form = BaseFormPluginForm
    model = BaseFormPlugin

    def render(self, context, instance, placeholder):
        self.render_template = 'aldryn_constantcontact/plugins/%s' % instance.template.name
        context['instance'] = instance
        return context

    def get_plugin_urls(self):
        return patterns('',
            url(r'^submit-form/$', submit_form, name='submit-form'),
        )

plugin_pool.register_plugin(EmailFormCMSPlugin)

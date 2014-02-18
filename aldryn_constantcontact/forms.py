# -*- coding: utf-8 -*-
from django import forms

from .models import BaseFormPlugin


class BaseFormPluginForm(forms.ModelForm):
    model = BaseFormPlugin

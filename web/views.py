# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    context = {}
    return render(request, 'index.html', context)


def login(request):
    context = {}
    if request.GET:
        return render(request, 'login.html', context)

    if request.POST:
        pass

from functools import wraps
from functools import partial
import asyncio
import requests
import json
import jwt
from django.utils import translation
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, permission_required, isAuthenticated
from . import dashboard

@authentication_required
@permission_required(permission = "app.statistics")
async def appStatistic(request):
  return render(request, 'app/app-statistic.html', {'title': gettext("app.statistic.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/app/app-statistic.css']})
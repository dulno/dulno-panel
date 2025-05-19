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
@permission_required(permission = "statistics.find")
async def statistic(request):
  return render(request, 'statistic/statistic.html', {'title': gettext("statistic.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/statistic/statistic.css']})
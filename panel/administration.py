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
@permission_required(permission = "groups.find")
async def administration(request):
  return render(request, 'administration/administration.html', {'title': gettext("panel.administration.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/administration/administration.css']})

@authentication_required
@permission_required(permission = "groups.find")
async def group(request, name):
  return render(request, 'administration/group.html', {'title': gettext("panel.group.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/administration/group.css'],
    'group': name})

@permission_required(permission = "staff.find")
@authentication_required
async def staff(request, id):
  return render(request, 'administration/staff.html', {'title': gettext("panel.staff.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/administration/staff.css'],
    'staff': id})
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, permission_required, isAuthenticated

@authentication_required
@permission_required(permission = "offer.find")
async def offer(request, id):
  return render(request, 'offer/offer.html', {'title': gettext("offer.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/offer/offer.css'],
     'offer': id})

@authentication_required
@permission_required(permission = "offer.create")
async def createOffer(request, id):
  return render(request, 'offer/offer-create.html', {'title': gettext("offer.create.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/offer/offer-create.css'],
      'partner': id})
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, permission_required, isAuthenticated

@authentication_required
@permission_required(permission = "partner.list")
async def partners(request):
  return render(request, 'partner/partners.html', {'title': gettext("partners.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/partner/partners.css']})

@authentication_required
@permission_required(permission = "partner.find")
async def partnerGeneral(request, id):
  return render(request, 'partner/partner-general.html', {'title': gettext("partner.general.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/partner/partner-tab.css', 'css/panel/partner/partner-general.css'],
    'partner': id})

@authentication_required
@permission_required(permission = "stamps.find")
async def partnerStamps(request, id):
  return render(request, 'partner/partner-stamp.html', {'title': gettext("partner.stamp.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/partner/partner-tab.css', 'css/panel/partner/partner-stamp.css'],
    'partner': id})

@authentication_required
@permission_required(permission = "partner.locations.find")
async def partnerLocations(request, id):
  return render(request, 'partner/partner-location.html', {'title': gettext("partner.location.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/partner/partner-tab.css', 'css/panel/partner/partner-location.css'],
    'partner': id})

@authentication_required
@permission_required(permission = "partner.links.find")
async def partnerLinks(request, id):
  return render(request, 'partner/partner-link.html', {'title': gettext("partner.link.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/partner/partner-tab.css', 'css/panel/partner/partner-link.css'],
    'partner': id})

@authentication_required
@permission_required(permission = "partner.bundle.find")
async def partnerBundle(request, id):
  return render(request, 'partner/partner-bundle.html', {'title': gettext("partner.bundle.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/partner/partner-tab.css', 'css/panel/partner/partner-bundle.css'],
     'partner': id})

@authentication_required
@permission_required(permission = "partner.bundle.change")
async def partnerBundleChange(request, id):
  return render(request, 'partner/partner-bundle-change.html', {'title': gettext("partner.bundle.change.title"),
   'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/partner/partner-bundle-change.css'],
    'partner': id})

@authentication_required
@permission_required(permission = "partner.payments.find")
async def partnerPayment(request, id):
  return render(request, 'partner/partner-payment.html', {'title': gettext("partner.payment.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/partner/partner-tab.css', 'css/panel/partner/partner-payment.css'],
    'partner': id})

@authentication_required
@permission_required(permission = "offers.find")
async def partnerOffers(request, id):
  return render(request, 'partner/partner-offers.html', {'title': gettext("partner.offers.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/partner/partner-tab.css', 'css/panel/partner/partner-offers.css'],
     'partner': id})

@authentication_required
@permission_required(permission = "partner.termination.status")
async def partnerTermination(request, id):
  return render(request, 'partner/partner-termination.html', {'title': gettext("partner.termination.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/partner/partner-tab.css', 'css/panel/partner/partner-termination.css'],
     'partner': id})
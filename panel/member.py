from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, permission_required, isAuthenticated

@authentication_required
@permission_required(permission = "member.find")
async def memberGeneral(request, id):
  return render(request, 'member/member-general.html', {'title': gettext("member.general.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/member/member-tab.css', 'css/panel/member/member-general.css'],
    'member': id})

@authentication_required
@permission_required(permission = "member.mails.find")
async def memberMail(request, id):
  return render(request, 'member/member-mail.html', {'title': gettext("member.mail.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/member/member-tab.css', 'css/panel/member/member-mail.css'],
    'member': id})

@authentication_required
@permission_required(permission = "member.sessions.find")
async def memberSession(request, id):
  return render(request, 'member/member-session.html', {'title': gettext("member.session.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/member/member-tab.css', 'css/panel/member/member-session.css'],
    'member': id})
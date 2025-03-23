from django.urls import path, include
from . import verification

urlpatterns = [
  path('', verification.login),
  path('confirm/<str:staff>/<str:token>/', verification.confirm),
  path('password/reset/request/', verification.passwordResetRequest),
  path('password/reset/complete/<str:staff>/<str:token>/', verification.passwordResetComplete),
]
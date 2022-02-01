from django.urls import path
from .viewset import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
  path("main/", GameViewSet.as_view({'get':'list'})),
  path("main/<int:pk>/", GameViewSet.as_view({'get':'retrieve'})),
  path("review/", ReviewCreateViewSet.as_view({'post':'create'})),
  path("developer/", DeveloperViewSet.as_view({'get':'list'})),
  path("developer/<int:pk>/", DeveloperViewSet.as_view({'get':'retrieve'})),
])

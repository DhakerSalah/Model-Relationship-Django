from django.urls import path ,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('paradigms', views.ParadigmList)
router.register('languages', views.LanguageList)
router.register('programmers', views.ProgrammerList)

urlpatterns = [
    path('', include(router.urls)),
]
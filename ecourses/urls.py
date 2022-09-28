from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('courses', views.CoursesViewSet)
router.register('users', views.UserViewSet)
router.register('lessons', views.LessonsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

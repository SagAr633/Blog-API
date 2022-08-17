from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('posts',views.BlogViewSet,basename='posts')


urlpatterns = [

]+router.urls
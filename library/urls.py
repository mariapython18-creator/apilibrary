from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from books import views


router = DefaultRouter()
router.register('books', views.Booksoperations, basename='books')
router.register('users', views.UserAPIView, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),


    path('login/', obtain_auth_token, name='api-login'),
    path('logout/', views.LogoutAPI.as_view(), name='api-logout'),
    path('search/', views.SearchAPIView.as_view(), name='api-search'),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

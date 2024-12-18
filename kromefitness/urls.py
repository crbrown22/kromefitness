"""kromefitness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import settings
from user_profile import views as user_profile_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('krome.urls')),
    path('login/', auth_views.LoginView.as_view(template_name="user/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="user/logout.html"), name='logout'),
    path('register/', user_profile_views.register, name='user-register'),
    path('profile/', user_profile_views.profile, name='user-profile'),
    path('profile/update/', user_profile_views.profile_update, name='user-profile-update'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="user/password_reset.html"), name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"), name= 'password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"), name='password_reset_complete'),
    path('profile/delete/<int:pk>', user_profile_views.member_delete, name ='member-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

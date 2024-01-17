"""
URL configuration for creation_account_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from account_creation_app.views import create_account, show_account, get_accounts, see_informations, modify_profile, delete_account, login_user, home, logout_user

from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_account/', create_account, name='create_account'),
    path('show_account/<int:id>/showit', show_account, name='show_account'),
    path('get_accounts/', get_accounts, name='get_accounts'),
    path('see_informations/<int:id>/details', see_informations, name='see_informations'),
    path('modify_profile/<int:id>/modify', modify_profile, name='modify_profile'),
    path('delete_account/<int:id>/delete', delete_account, name='delete_account'),
    path('login_user/', login_user, name='login_user'),
    path('home/', home, name='home'),
    path('logout_user/', logout_user, name='logout_user'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

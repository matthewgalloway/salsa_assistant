"""salsa_project URL Configuration

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
from django.urls import path
from salsa_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('algo_practice/', views.algo_practice, name='algo_practice'),
    path('all_moves/', views.all_moves),
    path('all_combos/', views.all_combos),
    path('move_history/', views.move_history, name='move_history'),
    path('combo_history/', views.combo_history, name='combo_history'),

]

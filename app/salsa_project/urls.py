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
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('algo_practice/', views.algo_practice, name='algo_practice'),
    path('position_review/', views.position_review, name='position_review'),
    path('all_moves/', views.all_moves),
    path('all_combos/', views.all_combos),
    path('update_move_difficulty/<int:move_id>/', views.update_move_difficulty, name='update_move_difficulty'),
    path('move_history/', views.move_history, name='move_history'),
    path('position_history/', views.position_history, name='position_history'),
    path('combo_history/', views.combo_history, name='combo_history'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

]

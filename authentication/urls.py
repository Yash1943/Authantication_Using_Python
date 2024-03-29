from django.contrib import admin
from django.urls import path, include
from . import views
from .views import create_sport

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('admin1', views.admin1, name='admin1'),
    path('player', views.player, name='player'),
    path('organizor', views.organizor, name='organizor'),
    path('mysession', views.mysession, name='mysession'),
    path('joinedsessions', views.joinedsessions, name='joinedsessions'),
    path('cancel_sessions', views.cancel_sessions, name='cancel_sessions'),
    path('change_password', views.change_password, name='change_password'),
    path('report', views.report, name='report'),
    path('signin/?next=/admin1', views.signin, name='signin'),
     path('signin/', views.signin, name='signin'),
    path('create_sport', views.create_sport, name='create_sport'),
    # path('get_sports', views.get_sports, name='get_sports'),
    #  path('create_sport', create_sport, name='create_sport')
]
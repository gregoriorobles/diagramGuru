from django.contrib import admin
from django.urls import path, include
from app import views as app_views

urlpatterns = [
    path('admin', admin.site.urls),
    path('accounts', include("django.contrib.auth.urls")),
    path('login', app_views.login, name='login'),
    path('signup', app_views.signup, name='signup'),
    path('dashboard', app_views.show_dashboard, name='show_dashboard'),
    path('diagrams', app_views.diagram, name='diagrams'),
    path('show_model', app_views.show_model, name='show_model'),
    path('create_model', app_views.create_model, name='show_model'),
    path('', app_views.index_app, name='index_app'),
]


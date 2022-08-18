from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup_view, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('personal/', views.personal_view, name='personal'),
    path('edit/', views.edit_view, name='edit'),
    path('logout/', views.logout_view, name='logout'),


]

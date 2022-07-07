from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='sign_up'),
    path('login/', views.login_view, name='login'),

]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [ #註冊連結
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'), #讓PATH連到template_name指定的html
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('password-change', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'), name='password_change'),
    path('password-change-done', 
        auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name='password_reset'),
    path('password-reset-done', 
        auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('mlbData/', views.mlbData, name="mlbData"),
    path('mlbSO_HR/', views.mlbSO_HR, name='mlbSO_HR'),
    path('mlbBB_HR/', views.mlbBB_HR, name='mlbBB_HR'),
    path('npbData/', views.npbData, name="npbData"),

]


from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home' ),
    path('projects/', views.projects, name='proj' ),
    path('new_project', views.NewProject, name='NewProj' ),
    path('projdeetz/<str:trial>', views.projectDetails, name='Pjdeetz' ),
    path('Delete_project/<int:id>/', views.DelProject, name='DelProj' ),
    path('Update_project/<int:id>/', views.UpProject, name='UpProj' ),



    path('login', views.login_page, name='login'),
    path('logout', views.logout_page , name='logout'),
    path('signup', views.signup_auth , name='signup')

]
from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views 
urlpatterns = [
    path('s1/',views.main),
    path('',views.Add_show,name='Add_Show'),
    path('delete/<int:id>/',views.delete_data,name='Delete_Data'),
    path('<int:id>/',views.Update_data,name='Update_Data'),
    path('login/', views.user_login, name='user_login'),
    # path('logout/', views.user_logout, name='user_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.show_students, name='show_students'),
]

from django.urls import path
from . import views 

urlpatterns=[
    path('register',views.register_user,name='register'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('index/',views.index,name='index'),
    path('post/<str:pk>',views.post,name='post')
]


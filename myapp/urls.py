from django.urls import path
from myapp import views

urlpatterns = [
    
    path('',views.register,name="register"),
    path("user_login/",views.user_login,name="user_login"),
     path("home/",views.home,name='home'),
    path("user_logout/",views.user_logout,name='user_logout'),
    path("apply/",views.apply,name="apply"),
    path("dash/",views.dash,name="dash"),
    path('applied/',views.Apply,name="applied"),
    path('add_post/',views.addpost,name="add_post"),
    path('blog/',views.blog,name="blog")
    # path('blogdetail/<int:pk>/',views.blogdetail,name="blogdetail")
]
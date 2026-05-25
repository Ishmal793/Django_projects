
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.signup ,name='signuppage'),
    path('login/',views.login_view, name='login'),
    path('todopage/',views.todopage),
    path ('edit_todo/<int:sr_no>/',views.edit_todo ,name='edit_todo'),
    path('delete_todo/<int:sr_no>/',views.delete_todo, name='delete_todo'),
    path('siginout/',views.signout,name='signout'),
    
]

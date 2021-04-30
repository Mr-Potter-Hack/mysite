from django.contrib import admin
from django.urls import include, path
from . import views
from .views import BlogView, postdetailview , AddPostView, UpdatePostView, DeletePostView
from members.views import UserRegisterView, UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('websites', views.websites, name='websites'),
    path('contact', views.contact, name='contact'),


    #path('blog', views.blog, name='blog'),
    #Blog Starts
    path('blog', BlogView.as_view(), name='blog'),
    path('articles/<int:pk>', postdetailview.as_view(), name='articles-detail'),
    path('add_post/',AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete',DeletePostView.as_view(), name='delete_post'), 
    path ('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='password_change'),
    
]    



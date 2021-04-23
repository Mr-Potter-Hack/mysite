from django.contrib import admin
from django.urls import include, path
from . import views
from .views import BlogView, postdetailview



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('websites', views.websites, name='websites'),
    path('contact', views.contact, name='contact'),


    #path('blog', views.blog, name='blog'),
    #Blog Starts
    path('blog', BlogView.as_view(), name='blog'),
    path('articles/<int:pk>', postdetailview.as_view(), name='articles-detail')

]

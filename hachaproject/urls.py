
from django.contrib import admin
from django.urls import path
import hachaapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hachaapp.views.home, name="home"),
    path('blog/<int:blog_id>', hachaapp.views.detail, name="detail"),
    path('blog/new/', hachaapp.views.new, name='new'),
    path('blog/create/', hachaapp.views.create, name='create'),
]

from django.contrib import admin
from django.urls import path

from app.views import frontpage
from app.views import frontpage2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',frontpage, name='confirm'),
    path('test',frontpage2, name='confirm2'),
]

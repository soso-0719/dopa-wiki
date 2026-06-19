from django.contrib import admin
from django.urls import path, include
from helloworld.views import top

urlpatterns = [
    path('', top, name='top'),
    path('helloworld/', include('helloworld.urls')),
    path('admin/', admin.site.urls),
]
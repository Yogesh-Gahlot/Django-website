from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header = "RBU Ice Cream Admin"
admin.site.site_title = "RBU Ice Cream Admin Portal"
admin.site.index_title = "Welcome to RBU Ice Cream"

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include('home.urls'))
]

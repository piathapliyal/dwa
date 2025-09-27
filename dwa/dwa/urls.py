from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD

urlpatterns = [
=======
from core.views import home 

urlpatterns = [
    path('', home),  
>>>>>>> b78ad04 (Initial commit with Django project)
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')), 
]
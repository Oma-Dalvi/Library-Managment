from django.contrib import admin
from django.urls import path,include
from library.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path("library-",include(("library.urls",'library'),namespace="library")),
]

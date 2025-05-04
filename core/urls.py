
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>پروژه با موفقیت دیپلوی شد!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    path('', home),

]

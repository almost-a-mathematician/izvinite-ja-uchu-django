"""ht1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clown/111', views.index, kwargs = {"name":"Oleg", "age":43, "position":"clown"}),
    path('math/222', views.index1, kwargs = {"num":"7", "pow":"2", "answer":"49"}),
    path('human/333', views.index2, kwargs = {"eye":"👁", "mouth":"👄", "slash":"/", "forwardslash":"|", "hi":"приветик 🛀🏻"}),
]

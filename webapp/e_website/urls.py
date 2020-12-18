"""e_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.home,name='home'),
    url('^oauth/', include('social_django.urls', namespace='social')),
    #url('^', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    url(r'^sell$', views.sell,name='sell'),
    url(r'^logout/$',views.logout_app,name='logout'),
    url(r'^logout/$',views.logout_sell,name='logout'),
    #url(r'/login',views.login),
    #url(r'/home',views.home),
    #url(r'^product_detail/(?P<id>\d+)/$',views.product_detail,name='product_details'),
]



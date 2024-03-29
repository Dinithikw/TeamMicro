"""kyc_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from kyc.views import index
from kyc.views import office, personal, account, insertkyc, insertkyc1, update, edit_val, update_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('office', office),
    path('personal', personal),
    path('account', account),
    path('update', update, name="update"),
    path("update/<int:id>", update_data),
    path('edit/<int:id>', edit_val),
    path('insertkyc', insertkyc),
    path('insertkyc1', insertkyc1)
]

"""resume_project URL Configuration

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
from django.urls import path
from resume import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('create', views.create, name='create'),

    path('form1', views.form1, name='form1'),
    path('form2', views.form2, name='form2'),
    path('form3', views.form3, name='form3'),
    path('form4', views.form4, name='form4'),
    path('form5', views.form5, name='form5'),
    path('form6', views.form6, name='form6'),

    path('done/<int:pk>/<str:clear>/', views.done, name='done'),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('generatePdf/<int:pk>/', views.generate_pdf)
]

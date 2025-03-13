"""
URL configuration for website_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from college import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),

    path("certificate/",views.certificate,name="certificate"),
    path('application_form/',views.application_form,name='application_form'),
    path('fees/',views.fees,name='fees'),


    path("celebrity/",views.celebrity,name="celebrity"),
    path('exam_time_table/',views.exam_time_table,name='exam_time_table'),
    path('exam_result/',views.exam_result,name='exam_result'),


    path("gallery/",views.gallery,name="gallery"),
    path("video/",views.video,name="video"),
    path("map/",views.map,name="map"),
    path("feedback/",views.feedback_store,name="feedback"),



    path('admin_login/',views.admin_login,name='admin_login'),


    
    path('admin_on/',views.admin_on,name='admin_on'),
    path('store_data/',views.store_data,name='store_data'),

    path('addmision_store/',views.addmision_store,name='addmision_store'),
    path('result_store/',views.result_store,name='result_store'),
    path('staff_store/',views.staff_store,name='staff_store'),



    path('view_data/',views.view_data,name='view_data'),

    path("application_view",views.application_view,name="application_view"),
    path("staff_view",views.staff_view,name="staff_view"),
    path("exam_result_view",views.exam_result_view,name="exam_result_view"),
    path("addmision_view",views.addmision_view,name="addmision_view"),
    path("feedback_view",views.feedback_view,name="feedback_view"),



    path('deleteadd/<int:id>/',views.delete_add),
    path('deletefeedback/<int:id>/',views.delete_feed),
    path('deleteapp/<int:id>/',views.delete_app,),
    path('deletestaff/<int:id>/',views.delete_staff,),
    path('deleteresult/<int:id>/',views.delete_result,),



    path('updateaddmision/<int:id>/',views.update_addmision,name="updateaddmision"),
    path('updateresult/<int:id>/',views.update_result,name="updateresult"),
    path('updatestaff/<int:id>/',views.update_staff,name="updatestaff")


    
]

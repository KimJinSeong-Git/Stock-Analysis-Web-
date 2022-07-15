# 사용자가 접속하는 Path에 따라 그 접속, 요청을 누가, 어떻게 처리할지 결정하는 파일( Routing )
from django.contrib import admin
from django.urls import path, include

""" 시나리오
 - http:/127.0.0.1/
 - http:/127.0.0.1/app/

 - http:/127.0.0.1/create/
 - http:/127.0.0.1/read/1/
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]

"""autotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from product import productviews
from apitest import apiviews
from bug import bugviews
from set import setviews
from apptest import appviews
from webtest import webviews
from performance import performanceviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', apiviews.login),
    path('home/', apiviews.home),
    path('logout/', apiviews.logout),
    path('apitest_manage/', apiviews.apitest_manage),
    path('apistep_manage/', apiviews.apistep_manage, name='apistep_manage'),
    path('apis_manage/', apiviews.apis_manage),
    path('product_manage/', productviews.product_manage),
    path('bug_manage/', bugviews.bug_manage),
    path('apis_set_product/', setviews.apis_set_product),
    path('api_set_product/', setviews.api_set_product),
    path('apis_set_manage/', setviews.apis_set_manage, name='apis_set_manage'),
    path('api_set_manage/', setviews.api_set_manage, name='api_set_manage'),
    path('set_user/', setviews.set_user),
    path('appcase_manage/', appviews.appcase_manage),
    path('appcasestep_manage/', appviews.appcasestep_manage, name='appcasestep_manage'),
    path('webcase_manage/', webviews.webcase_manage),
    path('webcasestep_manage/', webviews.webcasestep_manage, name='webcasestep_manage'),
    path('apistest_report/', apiviews.apistest_report),
    path('apitest_report/', apiviews.apitest_report),
    path('apptest_report/', appviews.apptest_report),
    path('webtest_report/', webviews.webtest_report),
    path('apitest_search/', apiviews.apitest_search),
    path('left/', apiviews.left),
    path('apis_set_manage_search/', setviews.apis_set_manage_search),
    path('api_set_manage_search/', setviews.api_set_manage_search),
    path('set_user_search/', setviews.set_user_search),
    path('product_search/', productviews.product_search),
    path('apis_search/', apiviews.apis_search),
    path('apitest_search/', apiviews.apitest_search),
    path('apistep_search/', apiviews.apistep_search),
    path('bug_search/', bugviews.bug_search),
    path('appcase_search/', appviews.appcase_search),
    path('appcasestep_search/', appviews.appcasestep_search),
    path('webcase_search/', webviews.webcase_search),
    path('webcasestep_search/', webviews.webcasestep_search),
    path('welcome/', apiviews.welcome),
    path('test_report/', apiviews.test_report),
    path('login/', apiviews.login),
    path('signup/', apiviews.signup),
    path('signup/submit/', apiviews.signup_submit),
    path('apis_task_list/', apiviews.apis_task_list),
    path('api_task_list/', apiviews.api_task_list),
    path('app_task_list/', appviews.app_task_list),
    path('web_task_list/', webviews.web_task_list),
    path('apis_task_new/', apiviews.apis_task_new),
    path('api_task_new/', apiviews.api_task_new),
    path('app_task_new/', appviews.app_task_new),
    path('web_task_new/', webviews.web_task_new),
    path('apis_task_submit/', apiviews.apis_task_submit),
    path('api_task_submit/', apiviews.api_task_submit),
    path('app_task_submit/', appviews.app_task_submit),
    path('web_task_submit/', webviews.web_task_submit),
    path('apis_task_delete/', apiviews.apis_task_delete),
    path('api_task_delete/', apiviews.api_task_delete),
    path('app_task_delete/', appviews.app_task_delete),
    path('web_task_delete/', webviews.web_task_delete),
    path('apis_task_info/', apiviews.apis_task_info),
    path('api_task_info/', apiviews.api_task_info),
    path('app_task_info/', appviews.app_task_info),
    path('web_task_info/', webviews.web_task_info),
    path('apis_task_update/', apiviews.apis_task_update),
    path('api_task_update/', apiviews.api_task_update),
    path('app_task_update/', appviews.app_task_update),
    path('web_task_update/', webviews.web_task_update),
    path('apis_task_run/', apiviews.apis_task_run),
    path('apis_task_execute/', apiviews.apis_task_execute),
    path('api_task_run/', apiviews.api_task_run),
    path('api_task_execute/', apiviews.api_task_execute),
    path('app_task_run/', appviews.app_task_run),
    path('app_task_execute/', appviews.app_task_execute),
    path('web_task_run/', webviews.web_task_run),
    path('web_task_execute/', webviews.web_task_execute),
    path('performancetest_manage/', performanceviews.performancetest_manage),
    path('performancestep_manage/', performanceviews.performancestep_manage, name='performancestep_manage'),
    path('performancetest_search/', performanceviews.performancetest_search),
    path('performance_task_list/', performanceviews.performance_task_list),
    path('performance_task_new/', performanceviews.performance_task_new),
    path('performance_task_submit/', performanceviews.performance_task_submit),
    path('performance_task_delete/', performanceviews.performance_task_delete),
    path('performance_task_info/', performanceviews.performance_task_info),
    path('performance_task_update/', performanceviews.performance_task_update),
    path('performance_task_run/', performanceviews.performance_task_run),
    path('performance_task_execute/', performanceviews.performance_task_execute),
    path('performance_report/', performanceviews.performance_report),
    # path('performance_locust/', performanceviews.performance_locust),
]
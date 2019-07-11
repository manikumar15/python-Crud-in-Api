
from django.contrib import admin
from django.conf.urls import url,include
from apicrudapp import views
from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings


router=routers.DefaultRouter()

router.register('task',views.StudentViewSet)


urlpatterns = [
   url('admin/', admin.site.urls),
   url(r'',include(router.urls)),
]

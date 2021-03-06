from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

urlpatterns = [
     url('^$',views.welcome,name = 'home'),
     url(r'^instagram/profile$',views.profile,name='displayProfile'),
     # url(r'^images',views.image,name="images"),
     # url(r'^photo/images',views.image,name="images"),
     url(r'^instagram/prof/(\d+)',views.prof,name="prof"),
     url(r'^photo/image$', views.new_image, name='new_image'),     
          
# views.article_detail),    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
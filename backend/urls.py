from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/',include('api.urls.product_urls')),
    path('api/users/',include('api.urls.user_urls')),
    path('api/orders/', include('api.urls.order_urls')),
    path('',TemplateView.as_view(template_name='index.html'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
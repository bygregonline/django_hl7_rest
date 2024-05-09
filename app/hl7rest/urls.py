
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('server', views.server_info_view),
    path('ps', views.process_view),
    path('pip', views.server_installed_modules_view),
    path('', views.default_home_view),
    path('403', views._403_view),
    path('hl7', views.hl7_web_view, name='hl7'),
    path('headers', views.info_headers_view),
    path('form.html', views.render_form_view),
    path('server_time', views.server_date_view),



]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

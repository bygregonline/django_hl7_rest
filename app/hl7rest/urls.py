
from . import views
from django.urls import path

urlpatterns = [
    path('server', views.serverInfoView),
    path('ps', views.processView),
    path('pip', views.installedModulesView),
    path('', views.defaultHomeView),
    path('403', views._403View),
    path('hl7', views.hl7_web_view ,name='hl7'),
    path('headers', views.infoheadersView),
    path('form.html', views.render_form_View),


]

from . import views
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('services/', views.services,name='services'),
    path('accounts/', include('accounts.urls')),
    path('appointment/', include('appointment.urls')),
    path('dashboard/', include('dashboard.urls')),


    
    path('about/',views.about,name='about'),

    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

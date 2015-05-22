from django.conf.urls import patterns, include, url
from crop import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
                       #url(r'^$', views.Home.as_view()),
                       url(r'^admin/', include(admin.site.urls)),
                       (r'^grappelli/', include('grappelli.urls')),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

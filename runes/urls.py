"""
Runes Project URL Configuration

The `urlpatterns` list routes URLs to views.
"""

from digicure_viewer.urls import register_routes as register_digicure_routes
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from rest_framework import routers

from apps.runes_viewer.urls import register_routes as register_runes_routes

# Configure admin site
admin.site.index_title = _('admin.site.index_title')
admin.site.site_header = _('admin.site.site_header')
admin.site.site_title = _('admin.site.site_title')

# Create main router
router = routers.DefaultRouter()
register_digicure_routes(router)
register_runes_routes(router)

# Basic URL patterns
urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

# Add i18n patterns
urlpatterns += i18n_patterns(
    path('', include(router.urls)),
    path('admin/', admin.site.urls), 
    path('api/', include(router.urls)),
    prefix_default_language=False
)

# Static and media files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if getattr(settings, "ENABLE_DEBUG_TOOLBAR", False):
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns += debug_toolbar_urls()
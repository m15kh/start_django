
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
sitemaps = {
    "static": StaticViewSitemap,
    'blog':BlogSitemap
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("website.urls")),
    path("blog/", include("blog.urls")),

        path("sitemap.xml", sitemap, {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path('captcha/', include('captcha.urls')),

] 
    
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

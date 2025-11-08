from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('books/', include('bookshelf.urls')),
    path('admin/', admin.site.urls),
    path('accounts/'. include('django.contrib.auth.urls')),
    path('relationship_app/', include('relationship_app.urls')),
]

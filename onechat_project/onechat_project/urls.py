from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('core.urls')),
                  path('rooms/', include('rooms.urls')),
                  path('profile/', include('my_profile.urls')),
                  path('user/', include('user.urls'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

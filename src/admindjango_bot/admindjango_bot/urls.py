from admin_bot import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '<slug:model_name>/<int:start_id>:<int:end_id>/',
        views.get_constants,
        name='get_constant',
    ),
    path('<slug:model_name>/', views.list_constant, name='list_constants'),
    path(
        '<slug:model_name>/<int:id>/', views.get_constant, name='list_constant'
    ),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from erp_core.views import frappe_rpc
import importlib
import os

router = DefaultRouter()

# Dynamic registration of all ViewSets
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for app in os.listdir(backend_dir):
    if os.path.isdir(os.path.join(backend_dir, app)) and app not in ['core_backend', 'erp_core', '__pycache__']:
        try:
            models_module = importlib.import_module(f'{app}.models')
            for name, obj in models_module.__dict__.items():
                if name.endswith('ViewSet') and hasattr(obj, 'queryset'):
                    # e.g. ItemViewSet -> items
                    resource_name = name.replace('ViewSet', '').lower() + 's'
                    router.register(rf'{app}/{resource_name}', obj, basename=f'{app}-{resource_name}')
        except ImportError:
            pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/rpc/', frappe_rpc),
    path('api/', include(router.urls)),
]

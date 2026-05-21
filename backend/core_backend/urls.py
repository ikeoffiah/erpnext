from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from erp_core.views import frappe_rpc

router = DefaultRouter()

# In a real comprehensive migration, we would iterate and register all ViewSets
# For this foundation, we provide the RPC and API structure.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/rpc/', frappe_rpc),
    path('api/', include(router.urls)),
]

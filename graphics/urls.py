from django.urls import path
from .views import HistoryAdmin,  Graphics

urlpatterns = [
    path('admin_history/', HistoryAdmin.as_view(), name='admin_history'),
    path('graphics/', Graphics.as_view(), name= 'graphics' ),
]
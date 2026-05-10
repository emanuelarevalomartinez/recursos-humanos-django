from django.urls import path
from .views import UploadFile, ChargeData

urlpatterns = [
     path('manage_data/', UploadFile.as_view(), name = 'manage_data'),
     path('charge_file/', ChargeData.as_view(), name='charge_file' ),
     
]

from django.urls import path
from .views import CreateAe2, CreateAe3

urlpatterns = [
    path('ae2/', CreateAe2.as_view(), name='ae2' ),
    path('ae3/', CreateAe3.as_view(), name='ae3'),
]
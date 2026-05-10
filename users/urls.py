from django.urls import path
from .views import Login, AdminSession, SessionUser, HistoryUser, DeleteUser, ListUsers, Logout, UpdateUser, GetUser



urlpatterns = [
    path('',Login.as_view(), name="login"),
    path('user_session/', SessionUser.as_view(), name="user_session"),
    path('user_history/',HistoryUser.as_view(), name ='user_history'),
    path('admin_session/', AdminSession.as_view(), name="admin_session"),
    path('delete/', DeleteUser.as_view(), name='delete_user'),
    path('list/', ListUsers.as_view(), name='user_list'),
    path('logout/', Logout.as_view(), name='logout'),
    path('update_user/', UpdateUser.as_view(), name='update_user'),
    path('get_user/<uuid:uuid>/', GetUser.as_view(), name='get_user'),
]

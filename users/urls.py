from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user, name='create_user'),
    path('update/<int:user_id>/', views.update_user, name='update_user'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('forced_logout_status/<int:user_id>/', views.forced_logout_status, name='forced_logout_status'),

]

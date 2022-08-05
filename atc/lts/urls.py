from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('requests/', views.service_requests, name='services-requests-dashboard'),
    path('request-form/', views.request_form, name='new-request'),
    path('add-new-request/', views.add_new_request, name='add-new-request-action'),
    path('update/request/<int:request_id>/', views.update_request, name='update_request_action'),
    path('delete/request/<int:request_id>/', views.delete_request, name='delete_request'),

]
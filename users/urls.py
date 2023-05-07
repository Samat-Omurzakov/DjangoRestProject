from django.urls import path
from users import views

urlpatterns = [
    path('registration/', views.registration_api_view),
    path('authorization/', views.authorization_aip_view),
    # path('confirm/', views.confirm_api_view)
]
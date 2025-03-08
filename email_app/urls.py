# email_app/urls.py
from django.urls import path
from .views import send_dynamic_email_view

urlpatterns = [
    path('send-email/', send_dynamic_email_view, name='send_dynamic_email'),
    # ... other URLs
]

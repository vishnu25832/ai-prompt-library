from django.urls import path
from . import views

urlpatterns = [
    path('prompts/', views.prompts),
    path('prompts/<uuid:id>/', views.get_prompt),
]
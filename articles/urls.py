from django.urls import path
from django.views.generic import TemplateView


app_name = "articles"

urlpatterns = [
    path('', TemplateView.as_view(template_name='articles/index.html'), name='index'),
]
from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/index.html'), name='index'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    # path('<int:user_id>/result', views.result, name='result'),
    # path('<int:user_id>/details/', views.details, name='details'),
]

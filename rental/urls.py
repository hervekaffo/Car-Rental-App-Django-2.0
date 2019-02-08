from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cars'),
    path('<int:id>/', views.detail, name='car-details'),
    path('contact', views.contact, name='contact'),
    path('pricing', views.PricingView.as_view(), name='pricing'),
    path('post', views.post_car_detail, name='post_a_car'),
    path('settings', views.settings, name='dashboard'),
    path('settings/payment', views.settings_payment, name='dashboard_payment'),
    path('oldest', views.sort_by_oldest, name='sort_by_oldest'),
    path('about', views.about, name='about'),
]

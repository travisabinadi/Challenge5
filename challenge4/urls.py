from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('hobbies', views.hobbies, name="hobbies"),
    path('hobbies/<int:hobby_id>', views.hobbies_detail, name="hobbies_detail"),
    path('portfolio/<int:item_id>', views.portfolio_detail, name="portfolio_detail"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('contact', views.contact, name="contact"),
]
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('hobbies', views.hobbies, name="hobbies"),
    path('hobbies/<int:hobby_id>', views.hobbies_detail, name="hobbies_detail"),
    path('portfolio/<int:item_id>', views.portfolio_detail, name="portfolio_detail"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('contact', views.contact, name="contact"),
    path('portfolio/add-portfolio-item', views.add_portfolio_item, name="add_portfolio_item"),
    path('portfolio/update-portfolio-item/<int:item_id>', views.update_portfolio_item, name="update_portfolio_item"),
    path('portfolio/delete-portfolio-item/<int:item_id>', views.delete_portfolio_item, name="delete_portfolio_item"),
]
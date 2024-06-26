from django.urls import path
from . import views
from .views import create_portfolio, portfolio_detail, success_page, list_portfolios, fileout_view
urlpatterns = [
    path('', views.create_portfolio, name= 'create_portfolio'),
    path('portfolio/<int:id>/', views.portfolio_detail, name='portfolio_detail'),
    path('success/', views.success_page, name='success_page'),
    path('portfolios/', list_portfolios, name='list_portfolios'),
    path('create/', create_portfolio, name='create_portfolio'),
    path('about/', views.about_view, name='about'),
    path('resume/', views.resume, name='resume'),
    path('fileout/', views.fileout_view, name='fileout')
]

    
    
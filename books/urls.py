from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('buy/<int:book_id>/', views.buy_book, name='buy_book'),
    path('read/<int:book_id>/<int:chapter_num>/', views.read_book, name='read_book'),
    path('publish/', views.publish_book, name='publish_book'),
    path('dashboard/', views.author_dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
]
 

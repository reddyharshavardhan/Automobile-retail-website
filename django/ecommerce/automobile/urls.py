from django.urls import path
from . import views

from automobile.controller import authview
urlpatterns = [
    path("",views.home,name="home"),
    path('product-list', views.productlistAjax),
    path('collections',views.collections, name="collections"),
    path('collections/<str:slug>',views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview, name="productview"),
    path('register/',authview.register, name="register"),
    path('login/',authview.loginpage, name='loginpage'),
    path('logout/', authview.logoutpage, name="logout"),
    path('searchproduct',views.searchproduct, name="searchproduct"),
]
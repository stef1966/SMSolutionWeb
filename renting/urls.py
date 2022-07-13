from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_view, name="test"),
    path('navbar/', views.navbar, name="navbar"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('main/', views.main, name="main"),
    path('plan/', views.plan, name="plan"),
    path('dashboard/', views.dashboard, name="dashboard"),
    # path('companies/', views.company, name="companies"),
    path('company/', views.company_view, name="company"),
    path('map_all/', views.map_all_view, name="map_all"),
    path('map_alone/', views.map_alone_view, name="map_alone"),
    path('plan_alone/', views.plan_alone_view, name="plan_alone"),
    path('renting/<str:pk>', views.test, name="companys"),
    path('create-company/', views.createCompany, name="create-company"),
    # path('update-company/<str:pk>', views.updateCompany, name='update-company'),
    path('update-company/', views.updateCompany, name='update-company'),
    path('delete-company/<str:pk>', views.deleteCompany, name='delete-company'),
    path('list_clients/', views.listClients, name="listClients"),
    path('test/', views.testTemp, name="test")
]
from django.urls import path
from .views import *


urlpatterns = [
    path("",base,name="base"),
    path("Vakansi",VakansiListView.as_view(),name="list_vakan"),
    path("detail_vakan/<int:pk>",VakansiDetailView.as_view(),name="detail_vakan"),
    path("update_vakan/<int:pk>",VakansiUpdateView.as_view(),name="update_vakan"),
    path("create_vakan",VakansiCreateView.as_view(),name="create_vakan"),
    path("delete_vakan/<int:pk>",VakansiDeleteView.as_view(),name="delete_vakan"),
    
    path("Category",CategoryListView.as_view(),name="list_category"),
    path("detail_category/<int:pk>",CategoryDetailView.as_view(),name="detail_category"),
    path("update_category/<int:pk>",CategoryUpdateView.as_view(),name="update_category"),
    path("create_category",CategoryCreateView.as_view(),name="create_category"),
    path("delete_category/<int:pk>",CategoryDeleteView.as_view(),name="delete_category"),
    
    
    path("Application",ApplicationListView.as_view(),name="list_app"),
    path("detail_app/<int:pk>",ApplicationDetailView.as_view(),name="detail_app"),
    path("update_app/<int:pk>",ApplicationUpdateView.as_view(),name="update_app"),
    path("create_app",ApplicationCreateView.as_view(),name="create_app"),
    path("delete_app/<int:pk>",ApplicationDeleteView.as_view(),name="delete_app")

]

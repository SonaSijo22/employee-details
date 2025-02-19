from django.urls import path
from empapp import views
urlpatterns = [
    path("emp/add/",views.EmpAddView.as_view(),name="emp-add"),
    path("emp/all/",views.EmployeeListView.as_view(),name="emp-list"),
    path("emp/<int:pk>/",views.EmployeeDetailView.as_view(), name="emp-detail"),
    path("emp/<int:pk>/remove/", views.EmployeeDeleteView.as_view(), name="emp-delete"),
    path("emp/<int:pk>/change/", views.EmployeeUpdateView.as_view(), name="emp-update")   
]

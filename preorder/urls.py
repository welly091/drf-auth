from django.urls import path
from .views import PreorderListView, PreorderDetailView

urlpatterns = [
    path("", PreorderListView.as_view(), name="preorder_list"),
    path("<int:pk>/", PreorderDetailView.as_view(), name="preorder_detail"),
]
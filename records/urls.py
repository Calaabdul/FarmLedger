
from django.urls import path

from .views import (
    CategoryListView,
    ProduceCreateView,
    ProduceDeleteView,
    ProduceDetailView,
    ProduceListCreateView,
    ProduceListView,
    ProduceUpdateView,
)

urlpatterns = [
    # DRF API
    path('produce/', ProduceListCreateView.as_view(), name='produce-api'),
    path('produce/<int:pk>/', ProduceDetailView.as_view(), name='produce-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),

    # Website pages
    path('manage/', ProduceListView.as_view(), name='produce-list'),
    path('manage/add/', ProduceCreateView.as_view(), name='produce-create'),
    path('manage/<int:pk>/edit/', ProduceUpdateView.as_view(), name='produce-update'),
    path('manage/<int:pk>/delete/', ProduceDeleteView.as_view(), name='produce-delete'),
]

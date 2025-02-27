from django.urls import path
from .views import RecipeDetailView, RecipeListView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail')
]

app_name = "ledger"

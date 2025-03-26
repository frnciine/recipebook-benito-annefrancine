from django.contrib import admin
from .models import Recipe, RecipeIngredient, RecipeImage


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline,]
    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ('name', 'ingredients',)


admin.site.register(Recipe, RecipeAdmin)

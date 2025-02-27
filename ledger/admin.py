from django.contrib import admin
from .models import Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline,]
    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ('name', 'ingredients',)

admin.site.register(Recipe, RecipeAdmin)

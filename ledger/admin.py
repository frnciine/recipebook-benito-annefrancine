from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline,]
    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ('name', 'ingredients',)

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

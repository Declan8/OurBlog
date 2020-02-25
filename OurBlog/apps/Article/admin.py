from django.contrib import admin

# Register your models here.
from .models import Author,Article,Classify,Example

@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('name','type')
    search_fields = ('name','type')
    list_filter = ('name','type')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','age')
    search_fields = ('name','age')
    list_filter = ('name','age')
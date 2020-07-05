from django.contrib import admin
from perpustakaan.models import Book, Category
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ["title","author","publisher","category","price"]
    search_fields = ["title","author","publisher"]
    list_filter = ("category",)
    list_per_page = 4

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category","description"]
    search_fields = ["category","description"]
   
    list_per_page = 4

admin.site.register(Book,BookAdmin)
admin.site.register(Category,CategoryAdmin)

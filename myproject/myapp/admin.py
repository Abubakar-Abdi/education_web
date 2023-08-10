from django.contrib import admin
from .models import contact1,Post
# Register your models here.
admin.site.register(contact1)
class postAdmin(admin.ModelAdmin):
    list_display=('title','slug', 'status','created_on')
    list_filter=("status",)
    search_fields=["title","content"]
    prepopulated_fields={"slug":("title",)}
admin.site.register(Post, postAdmin)

from django.contrib import admin

from .models import blog,history

# Register your models here.
@admin.register(blog)
class blogadmin(admin.ModelAdmin):
    list_display = ('id','title','desc')

@admin.register(history)
class historyadmin(admin.ModelAdmin):
    list_display = ('id','user','search_content')
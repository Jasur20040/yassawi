from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

class KyrsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Kyrs, KyrsAdmin)
admin.site.register(Reviews)
admin.site.register(Lesson)
admin.site.register(Test)

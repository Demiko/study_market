from django.contrib import admin
import store.models as m
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(m.Product,ProductAdmin)
admin.site.register(m.User)
admin.site.register(m.Cart)
admin.site.register(m.Tag, TagsAdmin)



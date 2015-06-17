from django.contrib import admin
from  .models  import BBS,Category,BBS_user

class BBS_admin(admin.ModelAdmin):
    list_display=('title','summary','author','signature','view_count','created_at')
    list_filter=('created_at',)
    search_fields=('title','author__user__username')

    def signature(self,obj):
        return obj.author.signature
    signature.short_description='hah'

class Category_admin(admin.ModelAdmin):
    list_display=('name','administrator')
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
# Register your models here.
admin.site.register(BBS,BBS_admin)
admin.site.register(Category,Category_admin)
admin.site.register(BBS_user)

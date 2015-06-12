from django.contrib import admin
from  .models  import BBS,Category,BBS_user

class BBS_admin(admin.ModelAdmin):
    list_display=('title','summary','author','signature','view_count','created_at')
    list_filter=('created_at',)
    search_fields=('title','author__user__username')

    def signature(self,obj):
        return obj.author.signature
    signature.short_description='hah'
    
# Register your models here.
admin.site.register(BBS,BBS_admin)
admin.site.register(Category)
admin.site.register(BBS_user)

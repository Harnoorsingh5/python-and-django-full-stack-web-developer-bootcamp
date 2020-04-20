from django.contrib import admin
from first_app.models import Topic,Webpage,AccessRecord
# Register your models here.

class WebpageAdmin(admin.ModelAdmin):
    fields = ['url','name','topic']
    search_fields = ['name']
    list_filter = ['name','topic']
    list_display = ['name','url','topic']
    list_editable = ['url']
admin.site.register(AccessRecord)
admin.site.register(Webpage, WebpageAdmin)
admin.site.register(Topic)
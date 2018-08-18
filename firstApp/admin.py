from django.contrib import admin

from firstApp.models import Article,Contact,Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )
admin.site.register(Contact, ContactAdmin)
admin.site.register([Article, Tag])

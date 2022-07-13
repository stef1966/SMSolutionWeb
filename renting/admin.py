from django.contrib import admin
from .models import Project, Review, Tag
from .models import Language, RealEstate, RealEstate_Company, Company

class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference', 'sentence_en', 'sentence_fr')

class SettingRealestateAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'draw_shape', 'length', 'width')

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)

admin.site.register(Language, SettingAdmin)
admin.site.register(RealEstate, SettingRealestateAdmin)
admin.site.register(RealEstate_Company)
admin.site.register(Company)

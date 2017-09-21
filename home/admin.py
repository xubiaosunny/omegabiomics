from django.contrib import admin
from home.models import *
# Register your models here.


class CarouselAdmin(admin.ModelAdmin):
    list_display=('id','img','link','display')


admin.site.register(Carousel, CarouselAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display=('id',)


admin.site.register(Company, CompanyAdmin)


class ModuleImgAdmin(admin.ModelAdmin):
    list_display=('id',)


admin.site.register(ModuleImg, ModuleImgAdmin)
from django.contrib import admin
from . models import *

# Register your models here.

class CompanyProfileAdmin(admin.ModelAdmin):
        list_display = ['id','name','phone','email','address']

class ApplicationChoiceAdmin(admin.ModelAdmin):
    list_display = ['id','type','item_img']
    prepopulated_fields = {'slug':('type',)}
    
class ApplicationAdmin(admin.ModelAdmin):
        list_display = ['id','full_name','email','address']


class UploadAdmin(admin.ModelAdmin):
        list_display = ['id','screenshot','time']





admin.site.register(CompanyProfile,CompanyProfileAdmin) 
admin.site.register(ApplicationChoice,ApplicationChoiceAdmin) 
admin.site.register(Application,ApplicationAdmin) 
admin.site.register(Upload,UploadAdmin) 
admin.site.register(ThanksEdit) 
admin.site.register(BtcInfo) 
admin.site.register(BnbInfo) 
admin.site.register(DogeInfo) 
admin.site.register(Contact) 
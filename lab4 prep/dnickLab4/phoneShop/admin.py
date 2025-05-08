from django.contrib import admin

from phoneShop.models import MobilenUred, Proizvoditel


# Register your models here.

class MobilenUredAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(MobilenUredAdmin, self).save_model(request, obj, form, change)




admin.site.register(MobilenUred, MobilenUredAdmin)
admin.site.register(Proizvoditel)
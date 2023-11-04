from django.contrib import admin

from admin_bot.models import AboutFundKeyboard, BasicInfoKeyboard, Keyboard


class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('keyboard_name', 'keyboard_text')
    empty_value_display = '-пусто-'
    # readonly_fields = ('keyboard_name',)

    class Meta:
        abstract = True


myModels = [AboutFundKeyboard, BasicInfoKeyboard, Keyboard]
admin.site.register(myModels, BaseModelAdmin)

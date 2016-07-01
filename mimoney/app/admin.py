from django.contrib import admin
from . import models

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
	fields = ('user', 'balance')

class MovementAdmin(admin.ModelAdmin):
	fields = ('user', 'concept', 'amount', 'date', 'contribution', 'done')

admin.site.register(models.Account, AccountAdmin)
admin.site.register(models.Movement, MovementAdmin)
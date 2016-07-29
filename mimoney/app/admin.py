from django.contrib import admin
from . import models

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
	fields = ('user', 'balance')

class MovementAdmin(admin.ModelAdmin):
	fields = ('user', 'concept', 'amount', 'contribution', 'done')
	readonly_fields = ('date',)

class RegularPaymentAdmin(admin.ModelAdmin):
	fields = ('user', 'concept', 'amount', 'contribution', 'done', 'next_payment')

admin.site.register(models.Account, AccountAdmin)
admin.site.register(models.Movement, MovementAdmin)
admin.site.register(models.RegularPayment, RegularPaymentAdmin)
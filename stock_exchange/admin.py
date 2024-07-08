from django.contrib import admin
from .models import Company, Buyer, Deal

# Регистрация модели Company
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'share_price', 'shares_available', 'controlling_stake')  # Поля для отображения в админке
    search_fields = ('name', 'address')  # Поля для поиска

# Регистрация модели Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'phone', 'email')  # Поля для отображения в админке
    search_fields = ('name', 'email')  # Поля для поиска

# Регистрация модели Deal
@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('deal_date', 'buyer', 'company', 'shares_quantity', 'deal_date')  # Поля для отображения в админке
    search_fields = ('buyer__name', 'company__name')  # Поля для поиска
    list_filter = ('deal_date',)  # Фильтры по полям

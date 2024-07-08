from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    share_price = models.DecimalField(max_digits=10, decimal_places=2)
    shares_available = models.IntegerField()
    controlling_stake = models.IntegerField()

    def __str__(self):
        return self.name

class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Deal(models.Model):
    deal_date = models.DateField(primary_key=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    shares_quantity = models.IntegerField()

    def __str__(self):
        return f"Deal {self.deal_date} - {self.buyer.name} - {self.company.name}"
from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    damaged = models.BooleanField(default=False)

    @property
    def status(self):
        order = Order.objects.filter(carId=self.id)
        if order.exists():
            if order.first().active:
                return "Rented"
            else:
                return "Booked"
        elif self.damaged:
            return "Damaged"
        else:
            return "Available"


    def __str__(self): 
        return str(self.id) + ' ' + self.make + ' ' + self.carmodel + ' ' + self.year + ' ' + self.location + ' ' + self.status

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + self.age + ' ' + self.address

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + self.address + ' ' + self.branch

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    carId = models.ForeignKey(Car, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' ' + str(self.customerId) + ' ' + str(self.carId) + ' ' + str(self.active)

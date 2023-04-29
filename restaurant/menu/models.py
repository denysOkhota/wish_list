from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        app_label = 'menu'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.restaurant.get_absolute_url()


class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    date = models.DateField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0, editable=False)

    class Meta:
        app_label = 'menu'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.restaurant.get_absolute_url()



class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        app_label = 'menu'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.restaurant.get_absolute_url()

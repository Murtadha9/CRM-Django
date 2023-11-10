from django.db import models


class Client(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=300)
    country=models.CharField(max_length=300)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name +' '+ self.last_name






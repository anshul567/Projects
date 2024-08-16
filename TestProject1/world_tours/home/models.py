from django.db import models # type: ignore

# Create your models here.


class Tour(models.Model):

    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.FloatField()


    def __str__(self) -> str:
        return (f"ID: {self.id} from {self.origin_country} to {self.destination_country} for {self.number_of_nights} in ${self.price} price")

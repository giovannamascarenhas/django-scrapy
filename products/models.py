from django.db import models


class NastyGalModel(models.Model):
    title = models.CharField(max_length=200, help_text="Product Title")
    original_price = models.CharField(max_length=200, help_text="Original Price")
    sale_price = models.CharField(max_length=200, help_text="Sale Price")

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
class PortfolioItem(models.Model):

    def __str__(self):
        return self.item_name

    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=200)
    item_image = models.CharField(max_length=500, default="https://media.istockphoto.com/photos/to-do-list-in-spiral-notepad-isolated-on-desk-picture-id1330040188?b=1&k=20&m=1330040188&s=170667a&w=0&h=3qCVSmD_-jOhmekoFh_0oH5KYGEjvcaK2azWkT-ZRYU=")

class Hobby(models.Model):

    def __str__(self):
        return self.hobby_name

    hobby_id = models.AutoField(primary_key=True)
    hobby_name = models.CharField(max_length=100)
    hobby_description = models.CharField(max_length=200)
    hobby_image = models.CharField(max_length=500, default="data:image/jpeg;base64,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")


class Contact(models.Model):

    def __str__(self):
        return self.name

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)
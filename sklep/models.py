from django.contrib.auth.models import User
from django.db import models


TYPES = (
    (1, "cat"),
    (2, "dog"),
)


class Animal(models.Model):
    type = models.IntegerField(choices=TYPES)
    name = models.CharField(max_length=64)
    description = models.TextField()
    age = models.DecimalField(max_digits=3, decimal_places=1)


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField()


class Donation(models.Model):
    name = models.CharField(max_length=64, default="Anonymous")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    message = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-publish', )


class Comments(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="comments")
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ("-publish", )


class TemporaryHome(models.Model):
    date = models.DateField()
    is_active = models.BooleanField(default=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='temp')


class Information(models.Model):
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=28)
    description = models.TextField()

    class Meta:
        ordering = ('-date', )

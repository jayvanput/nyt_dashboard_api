from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Entry(models.Model):
    puzzle_date = models.DateField()
    solve_date = models.DateField()
    elapsed_seconds = models.IntegerField()
    checked = models.BooleanField()
    revealed = models.BooleanField()
    streak = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-solve_date"]
        verbose_name_plural = "entries"
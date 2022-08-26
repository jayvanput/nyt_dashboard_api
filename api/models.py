from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Entry(models.Model):

    WEEKDAYS = [(1, "Sunday"), (2, "Monday"), (3, "Tuesday"), (4, "Wednesday"), (5, "Thursday"), (6, "Friday"), (7, "Saturday")]

    puzzle_date = models.DateField()
    solve_date = models.DateField()
    elapsed_seconds = models.IntegerField()
    used_help = models.BooleanField()
    streak = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=9,choices=WEEKDAYS,default=1)

    class Meta:
        ordering = ["-solve_date"]
        verbose_name_plural = "entries"
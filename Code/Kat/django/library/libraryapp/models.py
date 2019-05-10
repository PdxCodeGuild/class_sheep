from django.db import models
import datetime

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title_text = models.CharField(max_length=500)
    check_out_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_text

    def due_date_str(self):
        two_weeks = datetime.timedelta(days=14)
        return self.check_out_date + two_weeks

    def is_checked_out(self):
        if self.check_out_date is None:
            return "No"
        else:
            return "Yes"

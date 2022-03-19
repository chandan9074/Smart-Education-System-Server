from django.db import models
from accounts.models import StudentPorfile
from courses.models import Classes
# Create your models here.


class YearlyResult(models.Model):
    comments={
        ("Excellent","Excellent"),
        ("Very Good","Very Good"),
        ("Good","Good"),
        ("Average","Average"),
        ("Bellow Average","Bellow Average"),
        ("Poor","Poor"),
    }

    marks=models.IntegerField()
    total_marks=models.IntegerField()
    percentage=models.FloatField(blank=True,null=True)
    comments=models.CharField(max_length=50, choices=comments)
    class_name=models.ForeignKey(Classes, on_delete=models.CASCADE)
    students=models.ForeignKey(StudentPorfile, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.percentage:
                self.identity = (self.marks/self.total_marks)*100

        super(YearlyResult, self).save(*args, **kwargs)

    def __str__(self):
        return self.students.user.username


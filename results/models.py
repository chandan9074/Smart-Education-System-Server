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
    comments=models.CharField(max_length=50, choices=comments, blank=True, null=True)
    class_name=models.ForeignKey(Classes, on_delete=models.CASCADE)
    students=models.ForeignKey(StudentPorfile, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        percentage=(self.marks/self.total_marks)*100
        
        self.percentage = "{:.2f}".format(percentage)
        
        if  percentage>=80:
            self.comments = "Excellent"
        elif percentage >=70 and percentage<80:
            self.comments = "Very Good"
        elif percentage >=60 and percentage<70:
            self.comments = "Good"
        elif percentage >=50 and percentage<60:
            self.comments = "Average"
        elif percentage >=40 and percentage<50:
            self.comments = "Bellow Average"
        elif percentage<40:
            self.comments = "Poor"

        super(YearlyResult, self).save(*args, **kwargs)

    def __str__(self):
        return self.students.user.username +" ("+ self.class_name.class_name+self.class_name.section+")"


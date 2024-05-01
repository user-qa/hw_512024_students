from django.db import models


class StudentModel(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    dob = models.DateField()

    gender_choices = (
        ('male', 'male'),
        ('female', 'female'),
    )

    gender = models.CharField(max_length=6, choices=gender_choices)

    course_choices = (
        (1, 'first'),
        (2, 'second'),
        (3, 'third'),
        (4, 'fourth'),
    )

    course = models.IntegerField(choices=course_choices)


    passport = models.FileField(upload_to='media/passports', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_At = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

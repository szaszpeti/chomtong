from django.db import models
from django.urls import reverse_lazy, reverse
# Create your models here.
class Meditater(models.Model):
    year = models.CharField(max_length=264)
    course_type = models.CharField(max_length=120)
    name = models.CharField(max_length=20)
    state = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=60)
    gender = models.CharField(max_length=60)
    born = models.CharField(max_length=60)
    profession = models.CharField(max_length=60)
    remarks = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse("meditater:meditater_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("meditater:meditater_delete", kwargs={"pk": self.id})

    def get_email_url(self):
        return reverse("meditater:email_formating", kwargs={"pk": self.id})

    def get_sendingemail_url(self):
        return reverse("meditater:send_email", kwargs={"pk": self.id})





# class Email(models.Model):
#     sender = models.CharField(max_length=256)
#     subject = models.CharField(max_length=256)
#     message = models.CharField(max_length=1000)
#     meditater = models.ForeignKey(Meditater, related_name="meditaters", on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.sender
#
#     def get_absolut_url(self):
#         return reverse("meditater:meditater_detail", kwargs={"id": self.id})

# import csv
# import os
#
#
#
#
# with open('Student_List_2018.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     print(reader)
#     for row in reader:
#         p = Meditater(year=row["year"],
#                       course_type=row["course_type"],
#                       name=row["name"],
#                       state=row["state"],
#                       email=row["email"],
#                       gender=row["gender"],
#                       born=row["born"],
#                       profession=row["profession"])
#         p.save()

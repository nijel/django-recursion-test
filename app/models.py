from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    descriptions = models.TextField()
    notes = models.TextField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.descriptions)
        print(self.notes)


class Unit(models.Model):
    project = models.ForeignKey(Project, on_delete=models.RESTRICT)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def get_absolute_url(self):
        return f"{self.project.slug}/{self.slug}"

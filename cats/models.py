from django.db import models


class Cats(models.Model):
    cat_name = models.CharField(max_length=200)
    cat_nicknames = models.TextField()
    cat_dob = models.DateTimeField('Date of Birth')
    cat_image = models.ImageField(upload_to='images/', null=True)

    class Meta:
        verbose_name = "Cats"
        verbose_name_plural = "Cats"

    def __str__(self):
        return self.cat_name

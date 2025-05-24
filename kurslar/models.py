from django.db import models
from django.utils.text import slugify

class Kurs(models.Model):
    nomi = models.CharField(max_length=200)
    tavsif = models.TextField()
    narx = models.DecimalField(max_digits=10, decimal_places=2)
    rasm = models.ImageField(upload_to='kurs_rasmlari/')
    daraja = models.CharField(max_length=100, choices=[('boshlovchi', 'Boshlovchi'), ('orta', 'O‘rta'), ('ilgor', 'Ilg‘or')])
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nomi)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nomi

class Dars(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=200)
    video_url = models.URLField()
    tartib = models.PositiveIntegerField()

    class Meta:
        ordering = ['tartib']

    def __str__(self):
        return f"{self.kurs.nomi} - {self.nomi}"

# Create your models here.
from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=40)
    def __str__(self):
        return self.nama

# Create your models here.
class item(models.Model):
    nama = models.CharField(max_length=50)
    Deskripsi = models.TextField()
    jumlah = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.nama
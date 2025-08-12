from django.db import models

# Можно создать класс для базы данных
class Clinic(models.Model):
    title = models.CharField("Имя", max_length=10)
    phone = models.CharField("Телефон", max_length=30)
    describe = models.TextField("Опишите вашу проблему", max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title
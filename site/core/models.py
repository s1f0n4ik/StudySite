from django.db import models


class Speaker(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    photo = models.ImageField(upload_to='speakers/', verbose_name="Фотография",
                              help_text="Желательно квадратное изображение")
    position = models.CharField(max_length=300, verbose_name="Должность, опыт")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Спикер"
        verbose_name_plural = "Спикеры"
        ordering = ['id']


class ProgramModule(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название модуля/темы")
    description = models.TextField(verbose_name="Описание блока обучения")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок сортировки")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Модуль программы"
        verbose_name_plural = "Модули программы"
        ordering = ['order']


class Participant(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    university = models.CharField(max_length=255, verbose_name="Университет")
    faculty = models.CharField(max_length=255, verbose_name="Факультет")
    course = models.CharField(max_length=50, verbose_name="Курс обучения")
    email = models.EmailField(verbose_name="Электронная почта")
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return f"{self.full_name} ({self.email})"

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"
        ordering = ['-registered_at']
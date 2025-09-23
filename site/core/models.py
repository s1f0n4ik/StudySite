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

class SiteSettings(models.Model):
    header_background = models.ImageField(upload_to='backgrounds/', verbose_name="Фон для главного блока", blank=True, null=True)
    section_background = models.ImageField(upload_to='backgrounds/', verbose_name="Фон для светлых секций", blank=True, null=True)
    map_latitude = models.FloatField(verbose_name="Широта центра карты", blank=True, null=True,
                                     help_text="Например: 59.969240")
    map_longitude = models.FloatField(verbose_name="Долгота центра карты", blank=True, null=True,
                                      help_text="Например: 30.316317")
    map_zoom = models.PositiveSmallIntegerField(verbose_name="Масштаб карты", default=16,
                                                help_text="Значение от 1 до 19. Оптимально: 16-17.")

    def __str__(self):
        return "Настройки сайта"

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"
from django.db import models
from embed_video.fields import EmbedVideoField


class News(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='newsImage/main/')
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = "Новости"
        verbose_name = "Новости"


class NewsImage(models.Model):
    image = models.FileField(upload_to='newsImage/all/')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="News")

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name_plural = "Галерея новостей"
        verbose_name = "Галерея новостей"


class AchieveEvents(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    description = models.TextField(default='')
    result = models.TextField(default='Результаты будут позже')
    image = models.ImageField('achieve/main/')
    video = EmbedVideoField(blank=True, null=True)


class AchieveEventsImage(models.Model):
    image = models.FileField(upload_to='achieveImage/all/')
    achieve = models.ForeignKey(AchieveEvents, on_delete=models.CASCADE)

    def __str__(self):
        return self.achieve.name

    class Meta:
        verbose_name_plural = "Галерея прошедших турниров"
        verbose_name = "Галерея прошедшиъ турниров"


class Turnir(models.Model):
    title = models.CharField(max_length=250)
    events_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=250)
    description = models.TextField(default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Предстоящие турнир"
        verbose_name = "Предстоящие турниры"


class Sportsmen(models.Model):
    name = models.CharField(max_length=253)
    image = models.ImageField(upload_to='avatars/')
    age = models.IntegerField()
    fight = models.IntegerField()
    wins = models.IntegerField()
    weight = models.FloatField()
    weight_category = models.ForeignKey('WeightCategory', on_delete=models.CASCADE)
    pol = models.ForeignKey('Pol', on_delete=models.CASCADE)
    rating_total = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Спортсмен"
        verbose_name = "Спортсмены"


class WeightCategory(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Весовые категории"
        verbose_name = "Весовые категории"


class Pol(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "пол"
        verbose_name = "пол"


class Coach(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField(default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "тренеры"
        verbose_name = "тренер"


class Donate(models.Model):
    bank_account = models.CharField(max_length=255)
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)

    def __str__(self):
        return self.bank_account

    class Meta:
        verbose_name_plural = "реквизиты"
        verbose_name = "реквизит"


class Bank(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "банки"
        verbose_name = "банк"



from django.db import models


class Genre(models.Model):
  """Жанр"""

  name = models.CharField("Имя", max_length=100)
  url = models.SlugField(max_length=100, unique=True)

  def __str__(self) -> str:
      return self.name

  class Meta:
    verbose_name = "Жанр"
    verbose_name_plural = "Жанры"


class Platform(models.Model):
  """Игровая платформа"""

  name = models.CharField("Имя", max_length=100)

  def __str__(self) -> str:
      return self.name

  class Meta:
    verbose_name = "Игровая платформа"
    verbose_name_plural = "Игровые платформы"


class Developer(models.Model):
  """Разбработчики и издатели"""

  name = models.CharField("Имя", max_length=100)
  description = models.TextField("Описание", max_length=255)
  logo = models.ImageField("Логотип", upload_to="logo/")

  def __str__(self) -> str:
      return self.name

  class Meta:
    verbose_name = "Разработчик"
    verbose_name_plural = "Разработчики"


class Game(models.Model):
  """Игра"""

  title = models.CharField("Имя", max_length=100)
  description = models.TextField("Описание", max_length=6000)
  release_date = models.DateField("Дата выхода")
  genre = models.ManyToManyField(Genre, verbose_name="Жанр", related_name="game_genre")
  developer = models.ManyToManyField(Developer, verbose_name="Разработчик", related_name="game_developer")
  publisher = models.ManyToManyField(Developer, verbose_name="Издатель", related_name="game_publisher")
  platform = models.ManyToManyField(Platform, verbose_name="Платформа", related_name="game_platform")
  site = models.CharField("Сайт", max_length=100)
  trailer = models.CharField("Трейлер", blank=True, max_length=100)
  url = models.SlugField(max_length=100, unique=True)
  poster = models.ImageField("Постер", upload_to="media/", default='SOME STRING')

  def __str__(self) -> str:
      return self.title

  class Meta:
    verbose_name = "Игра"
    verbose_name_plural = "Игры"


class GameScreenShots(models.Model):
  """Скриншоты из игры"""

  title = models.CharField("Имя", max_length=100)
  image = models.ImageField("Изображение", upload_to="image/")
  game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="Игра")

  def __str__(self) -> str:
      return self.title

  class Meta:
    verbose_name = "Скриншот"
    verbose_name_plural = "Скриншоты"


class RatingStar(models.Model):
  """Звезда рейтинга"""
  
  value = models.PositiveSmallIntegerField("Значение", default=0)

  def __str__(self) -> str:
      return self.value

  class Meta:
    verbose_name = "Звезда рейтинга"
    verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
  """Звезда рейтинга"""

  ip = models.CharField("IP адрес", max_length=100)
  star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Звезда")
  game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="Игра")

  def __str__(self) -> str:
      return f'{self.star} - {self.game}'

  class Meta:
    verbose_name = "Рейтинг"
    verbose_name_plural = "Рейтинги"


class Review(models.Model):
  """Рецензии"""
  
  email= models.EmailField()
  name = models.CharField("Имя", max_length=100)
  text = models.TextField("Рецензия", max_length=6000)
  game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="Игра", related_name="reviews")
  parent = models.ForeignKey(
    'self', on_delete=models.SET_NULL, verbose_name="Предыдущий_коммент", blank=True, null=True,
    related_name="children")

  def __str__(self) -> str:
      return f'{self.name} - {self.game}'

  class Meta:
    verbose_name = "Рецензия"
    verbose_name_plural = "Рецензии"

from django.db import models
from django.db.models import TextChoices


class Themes(TextChoices):
    art = "Art et littérature"
    divertissement = "Divertissement"
    geographie = "Géographie"
    histoire = "Histoire"
    sport = "Sport"
    loisirs = "Loisirs"
    sciences = "Sciences"


class QuestionReponse(models.Model):
    enonce = models.TextField()
    reponse = models.TextField()
    repondu = models.BooleanField(default=False)
    theme = models.CharField(max_length=50, choices=Themes.choices, default=Themes.sciences)

    def __str__(self):
        return str(self.id)+" - "+self.enonce[:20]
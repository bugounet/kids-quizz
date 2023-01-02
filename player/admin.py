from django.contrib import admin
from .models import QuestionReponse

# Register your models here.

@admin.register(QuestionReponse)
class QuestionReponseAdmin(admin.ModelAdmin):
    actions= ["remise_a_zero"]

    def remise_a_zero(self, *args, **kwargs):
        QuestionReponse.objects.all().update(repondu=False)

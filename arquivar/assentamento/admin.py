from django.contrib import admin

# my imports
from assentamento.models import AssentamentoFuncional, Situacao, PrateleiraFace, ArmarioAcervo, FaceArmario
# Register your models here.

@admin.register(AssentamentoFuncional, 
    Situacao,
    ArmarioAcervo,
    FaceArmario,
    PrateleiraFace)
    
class AssentamentoAdmin(admin.ModelAdmin):
    pass
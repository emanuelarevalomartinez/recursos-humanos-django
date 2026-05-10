from django.shortcuts import render
from django.views import View
from .models import File
from django.http  import JsonResponse
import pandas as pd
from exel_exports.models import Data
from django.conf import settings
import os
# Create your views here.
class UploadFile(View):

    def post(self, request):
        try:
         filename_input = request.POST.get('filename')
         file_input = request.FILES.get('file')
         ext = str(file_input).split('.')[1].lower()
         if filename_input and file_input and ext in ['xls','xlsx']:
          newfile = File(name = filename_input, file = file_input)
          newfile.save()
         else: return JsonResponse({ 'ok' : False, "message": "invalid format", })
         
         return JsonResponse({
            'ok': True,
            'message': "file uploaded"
          }) 
        
        except Exception as error:
           return JsonResponse({
              'ok': False,
              'message': str(error)
           })
        


class ChargeData(View):
    
    template = 'uploads/charge_data.html'
    
    def get(self, request):
       return render(request,self.template)

    def post(self,request):
       try:
         dat = Data.objects.all()
         dat.delete()
         uploads = os.path.join(settings.MEDIA_ROOT,'uploads')
         
         file = [f for f in os.listdir(uploads) if f.endswith('.xlsx') or f.endswith('.xls')]

         if not file: return JsonResponse({ 'message': 'not found file' })
         
         namefile = file[0]
         path_reference = os.path.join(uploads,namefile)

         df = pd.read_excel(path_reference)
         for index, row in df.iterrows():
            newData = Data(
               id_empleado=row['Id_Empleado'],
               nombre=row['Nombre'],
               apellido_1=row['Apellido_1'],
               apellido_2=row['Apellido_2'],
               tipo_de_contrato=row['Desc_Tipo_Contrato'],
               categoria=row['Desc_Categoria'],
               subcategoria=row['Desc_Subcategoria'],
               cargo=row['Desc_Subcategoria'],
               categoria_di=row['Desc_Categoria_DI'],
               grado_cientifico=row['Desc_Grado_Cientifico'],
               sexo=row['Sexo'],
               direccion=row['Desc_Direccion'],
               fecha_nacimiento=row['Fecha_Nacimiento'],
               edad=row['Edad'],
               menor_o_igual_35=row['Es_Menor_Igual_35'],
               causa_alta=row['Id_CausaAlta'],
               nivel_escolaridad=row['Desc_Nivel_Escolaridad'],
               siglas=row['Siglas'],
               salario_basico=row['Salario_Basico'],
            )
            newData.save()
         
         return JsonResponse({
            'ok': True,
            'message': 'data ready'
         })

       except Exception as error:
          
        return JsonResponse({
           'ok': False,
           'message': str(error)
        })
       

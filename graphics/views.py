from django.views.generic import ListView
from django.views import View
from .models import History
from django.http import JsonResponse
import json
from exel_exports.models import Ae2, Ae3

# Create your views here.
class  HistoryAdmin(ListView):

    model = History
    template_name = 'history/admin_history.html'
    context_object_name = 'historial'
    paginate_by = 5
    ordering = 'date'

    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     paginator = context['paginator']
     page_obj = context['page_obj']
     context['page'] = page_obj.number
     context['num_pages'] = paginator.num_pages
     return context
    




class Graphics(View):
   flag = ''
   count = 0
  
   def post(self,request):
      try:
        #consultas a la base de datos
        data = json.loads(request.body.decode('utf-8'))
        init_date= data.get('sinceData')
        end_date= data.get('untilData')
        init_year = str(init_date).split('-')[0]
        init_moth = str(init_date).split('-')[1]
        init_day =  str(init_date).split('-')[2]
        
        end_year = str(end_date).split('-')[0]
        end_moth = str(end_date).split('-')[1]
        end_day = str(end_date).split('-')[2]
        
        document = data.get('typeTable')
        colum = data.get('colum')
        print(int(init_year),'  ',end_year)
        #values 
        month = []
        obj_anno_cols = []
        values = []
      
        if(document == 'ae2'):
          query = Ae2.objects.all().order_by('anno')
          for index in range (len(query.values())):
            if(int(init_year) == query.values()[index].get('anno')):
              self.flag = query.values()[index].get('anno')
            else :  query.values()[index].pop
          for value in query.values():
             if(self.flag == value.get('anno')): 
                self.count = self.count + 1
             else: 
               if(int(value.get('anno'))>= int(init_year) and int(value.get('anno'))<= int(end_year)): 
                 obj_anno_cols.append({ 
                    'title': self.flag,
                    'cols': self.count,
                  })
                 self.flag = value.get('anno')
                 self.count = 1
             if(int(value.get('anno'))>= int(init_year) and int(value.get('anno'))<= int(end_year)):
                  values.append(value.get(colum))
                  month.append(value.get('mes_creado'))
                  
        else: 
           query = Ae3.objects.all().order_by('anno')    
           self.flag = query.values()[0].get('anno')
           for index in range (len(query.values())):
            if(int(init_year) == query.values()[index].get('anno')):
              self.flag = query.values()[index].get('anno')
            else :  query.values()[index].pop
           for value in query.values():
             if(self.flag == value.get('anno')): 
               self.count = self.count + 1
             else: 
               if(int(value.get('anno'))>= int(init_year) and int(value.get('anno'))<= int(end_year)): 
                 obj_anno_cols.append({ 
                    'title': self.flag,
                    'cols': self.count,
                  })
                 self.flag = value.get('anno')
                 self.count = 1
             if(int(value.get('anno'))>= int(init_year) and int(value.get('anno'))<= int(end_year)):
                  values.append(value.get(colum))
                  month.append(value.get('mes_creado'))
        
        obj_anno_cols.append({ 
            'title': self.flag,
            'cols': self.count,
            })

        data_g = {
           'month': month,
           'obj_anno_cols': obj_anno_cols,
           'values' : values
        }

        return JsonResponse({
           'ok': True,
           'data_g': data_g,
           #valores para graficar pedir formato a emanuel
           
        })
      except Exception as error:
         return JsonResponse({
            'ok': False,
            'message': str(error)
         })
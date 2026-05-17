from .models import User     
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from django.http import JsonResponse
from django.views.generic import ListView
import json
from graphics.models import History
# Create your views here.
class Login(View):
    template_login ='login/login.html'
    def get(self, request):
      return render(request,self.template_login)
    
    def post(self, request):
      try:
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('username') 
        password = data.get('password').strip()
        user = User.objects.get(username = name)
    
        stored_password = user.password
        role = user.role
        is_valid = check_password(password, stored_password)
  
        if (is_valid and role == "admin"):
          return JsonResponse({ "ok": True, "adress":'admin_session/','auth': { 'key': 'autha', 'value': 'true'}})
        elif(is_valid): 
          return JsonResponse({ "ok": True, "adress":'user_session/', 'auth': { 'key': 'authu', 'value': 'true'} })
        else: return  JsonResponse({
          "ok": False,
          "message": 'wrong password'   
        })
      
      except Exception as error:
         return JsonResponse({
           'ok': False,
           'message': str(error)
         })
  

class AdminSession(View):
    template = 'admin/admin_session.html'
    user = User.objects

    def get(self, request):
      if( not request.COOKIES.get('autha')): return redirect('login')
      return render(request, self.template)

    def post(self,request):
      try:
       data = json.loads(request.body.decode('utf-8'))
       hashed_password = make_password(data.get('password').strip())
       email_input = data.get('email')
       name = data.get('username')
       self.user.create(username = name, email = email_input, password = hashed_password)
       return JsonResponse({ 'ok': True, 'message': "Usuario creado con exito"})
      except Exception as error:
        return JsonResponse({
          'ok': 'false',
          'message': str(error)
        })
      
   
class DeleteUser(View):

   def post(self, request):
      try:
      
       uuid = request.POST['uuid']
       user = User.objects.get(id = uuid)
       user.delete()
       return redirect('user_list')   
     
      except Exception as error:

        return JsonResponse({
          'ok': False,
           'message': str(error)
        })
    


class ListUsers(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'usuarios'
    paginate_by = 5
    ordering = 'email'

    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     paginator = context['paginator']
     page_obj = context['page_obj']
     context['page'] = page_obj.number
     context['num_pages'] = paginator.num_pages
     return context


class UpdateUser(View):
  
  user = User.objects

  def post(self, request):
    try: 
     data = json.loads(request.body.decode('utf-8'))
     id_input = data.get('id')
     email_input = data.get('email')
     password_input = make_password(data.get('password'))
     username_input = data.get('username')
     print(username_input)
     print(password_input)
     print(email_input)
     role_input = data.get('role')
     print(role_input)
     self.user.filter(id = id_input).update(email = email_input, 
                     username = username_input,
                     password = password_input,
                     role = role_input,
                     )
     return JsonResponse({
      'ok': True,
      'message': 'user update',
     })
    except Exception as error:
      return JsonResponse({
        'ok': False,
        'message': str(error)
      })
  

class GetUser(View):
   
  user = User.objects
  
  def get(self, request, *args, **kwargs):
    user = self.user.get(id = kwargs['uuid'] )
    username = user.username
    email = user.email
    role = user.role
    
    return JsonResponse({
      'username': username,
      'email': email,
      'role': role
    })

  
class HistoryUser(ListView):

    model = History
    template_name = 'history/user_history.html'
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
    

class SessionUser(View):
   template = 'user/user_session.html'

   def get(self, request):
      if( not request.COOKIES.get('authu')): return redirect('login')
      return render(request, self.template)


class Logout(View):
  
  def get(self,request):
    res = redirect('login')
    res.delete_cookie('authu')
    res.delete_cookie('autha')
    return res



  
 
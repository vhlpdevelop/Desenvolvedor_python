from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, CalculoForm
from .models import User, Calculo


def index(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, 'user/index.html', context=context)

def calculo(request):
   
    if request.method == 'POST':
     form = CalculoForm(request.POST)
     if form.is_valid():
      # some code here
      print(form.data['a'])
      a = float(form.data['a'])
      b = float(form.data['b'])
      c = float(form.data['c'])
      delta = (b ** 2) - 4 * a * c
      if a == 0:
          print("O valor de a, deve ser diferente de 0")
      elif delta < 0:
          print("Sem raízes reais")
          context={
          'form':form,
          'calculoResultA': 'ERRO',
          'calculoResultB': 'sem raizes reais'
          }
          return render(request, 'calculo/calculo.html', context=context)  
      else:
          x1 = (-b + delta ** (1 / 2)) / (2 * a)
          x2 = (-b - delta ** (1 / 2)) / (2 * a)
          context={
          'form':form,
          'calculoResultA': x1,
          'calculoResultB': x2
          }
          return render(request, 'calculo/calculo.html', context=context)
    else:
     form = CalculoForm()
    
    context = {
    'form': form,
    }
    return render(request, 'calculo/calculo.html', context=context)
  
   
       
        
           

def create(request):
    if(request.method == 'GET'):
        form = UserForm()
        #Importante!
        context = {
            'form': form,
        }
        return render(request, 'user/criar.html', context=context) #Context sendo enviado com formulario
    elif request.method =='POST':
        form = UserForm(request.POST)
        if(form.is_valid()):
           form.save()
           return redirect(index)
   
       
def modify(request, user_id):
    print(user_id)
    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        form = UserForm(data=request.POST,instance=user)
        if(form.is_valid()):
           form.save()
           return redirect(index)
    else:
        form = UserForm(instance=user)
        context = {'form':form}
        return render(request, 'user/criar.html', context=context)
    
           
def delete(request, user_id):
    print(user_id)

    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect(index)
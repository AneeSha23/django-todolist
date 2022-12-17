from django.shortcuts import redirect, render

from home.models import Todos

# Create your views here.
def index(request):
    if request.method == 'POST':
        list = request.POST['list']
        new_todo=Todos(list=list)
        new_todo.save()

    data=Todos.objects.all()
    return render(request,'index.html',{'Data':data})

def delete(request,id):
    data = Todos.objects.get(id=id)
    data.delete()
    return  redirect("index")
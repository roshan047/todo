from django.shortcuts import render,redirect
from insert.models import Task

def add(request):
    if(request.method=="POST"):
        heading_=request.POST['heading']
        detail_=request.POST['detail']
        date_=request.POST['date']
        print(heading_)
        print(detail_)
        print(date_)
        insert_data=Task.objects.create(heading=heading_,details=detail_,date=date_,is_deleted="no")
        insert_data.save()
        return redirect("/")

    return render(request,'insert/add.html')

def home(request):
    all_data=Task.objects.all()
    data={'show':all_data}
    return render(request,"insert/index.html",data)

def delete(request,tid):
    record=Task.objects.filter(id=tid)
    record.delete()
    return redirect('/')

# Create your views here.

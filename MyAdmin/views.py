from django.shortcuts import render
from MyAdmin.models import Form,Textfield
from django.http import JsonResponse
import json

# Create your views here.

def Form_View(req):
    return render(req,'generate.html')

def Save(request):
    print(request.GET['temp'])
    data = request.GET.get('temp','')
    y = json.loads(data)
    f = Form(Description="Demo8")
    f.save()
    print("form saved")
    print(y)
    l=[]
    for k in y:
        l.append(y[k])
    print(l)
    for i in range(0,len(l),2):
        print(l[i],l[i+1])
        t = Textfield(name=l[i],typ=l[i+1],form=f)
        t.save()
    return JsonResponse({'status':"success"})

def showforms(req):
    data=Form.objects.all()
    context={
        'forms':data,
    }
    return render(req,'showform.html',context=context)

def detailform(req):
    id = req.GET['id']
    f = Form.objects.get(Id=id)
    data = Textfield.objects.filter(form__pk=f.Id)
    #data = f.textfield_set.all()
    print(data)
    context={
        'alldata':data,
    }
    return render(req,'detailform.html',context=context)

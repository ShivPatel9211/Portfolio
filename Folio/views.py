from django.shortcuts import render ,HttpResponse ,redirect
from . models import Contact
from django.contrib import messages
def home(request):
    if request.method == 'POST':
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        mesg= request.POST['message']
        cont=Contact(name=name,email=email,phone=phone,messg=mesg)
        cont.save()
        messages.success(request,'Thank you !! for contacting me , I will answer you soon')
        return redirect('home')

    return render(request,'index.html')

from django.shortcuts import render, redirect
#from django.views.generic import TemaplateView
from .forms import BookForm
from .models import Book


def exp(request):
    return render(request,'exp.html'  )


def upload(request):
    context={}
    if request.method == 'POST' :
        uploaded_file=request.FILES.get('document')
        fs = FileSystemStorage()
        name=fs.save(uploaded_file.name, uploaded_file)
        context['url']=fs.url(name)
    return render(request,'upload.html' , context )
# Create your views here.

def book_list(request):
    books=Book.objects.all()
    return render(request,'book_list.html',{'books': books})



def upload_book(request):
    if request.method == 'POST' :
        form =BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else :
        form =BookForm()
    return render(request,'upload_book.html',{'form':form})

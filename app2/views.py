from django.shortcuts import render

# Create your views here.
def jinja_print2(request):
    d={'name':'Krishna'}
    return render(request,"jinja_print2.html",context=d)
from django.shortcuts import render

# Create your views here.
def helloWorld(request):
    context = {'greeting': 'Everyone !!'}
    return render(request,'hello.html',context)

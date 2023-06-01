from django.shortcuts import render

# Create your views here.
def condition(request):
    d ={'a':500,'b':1000,'c':200}
    return render(request,'condition.html',context=d)



def loop(request):
    d = {'name':'vandana'}
    return render(request,'loop.html',d)
